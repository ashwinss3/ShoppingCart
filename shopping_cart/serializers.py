from rest_framework import serializers
from .models import User, Product, Order, OrderItem, Payment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']  # Add more fields as needed
        extra_kwargs = {'password': {'write_only': True}}  # Make 'password' field write-only

    def create(self, validated_data):
        # Extract and set the password before creating the user
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data, password=password)
        return user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def validate(self, data):
        """
        Validate product quantity.
        """
        product = data.get('product')
        quantity = data.get('quantity')

        if product and quantity:
            if quantity > product.available_quantity:
                raise serializers.ValidationError("Not enough stock available for this product.")

        return data

    def create(self, validated_data):
        # Calculating the price of the order item
        price = validated_data['quantity'] * validated_data['product'].price

        # Calling super class to create the order item
        order_item = super().create(validated_data)

        # Update the price of the order
        order = order_item.order
        order.total_price += price
        order.save()

        return order_item


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

    @staticmethod
    def update_order_quantities(order):
        """
        Update product quantities in the order after payment.
        """
        order_items = order.orderitem_set.all()

        for order_item in order_items:
            product = order_item.product
            product.stock -= order_item.quantity
            product.save()

    def create(self, validated_data):
        """
        Create payment instance and update order quantities after payment.
        """
        payment = super().create(validated_data)

        # Retrieve the associated order
        order = payment.order

        # Check if payment status is 'completed'
        # Update product quantities in the order
        self.update_order_quantities(order)

        return payment

    def validate(self, data):
        """
        Validate product quantity.
        """
        order = data.get('order')
        payment_amount = data.get('order')

        if order:
            if order.total_amount > payment_amount:
                raise serializers.ValidationError("Payment amount less than order amount.")

        return data


# Django + DRF 模块级代码(需 INSTALLED_APPS 含 rest_framework)
try:
    from rest_framework import serializers
except ImportError:
    print("该题演示需要第三方库 djangorestframework:pip install djangorestframework(正文已讲清原理,安装后可运行)")
    raise SystemExit(0)

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)

    def validate_name(self, value: str) -> str:
        if not value.strip():
            raise serializers.ValidationError('name 不能为空')
        return value.strip()

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True)

    class Meta:
        model_name = 'Book'   # 实际代码写 model = Book
        fields = ['id', 'title', 'price', 'author', 'author_id']
        read_only_fields = ['id']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('price 必须大于 0')
        return value

    def create(self, validated_data):
        validated_data.pop('author_id', None)
        # 实际: return Book.objects.create(**validated_data)
        return validated_data

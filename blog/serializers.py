from rest_framework import serializers


class AllArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    cover = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=256)
    content = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=2048)
    created_at = serializers.DateTimeField(required=True, allow_null=False)
    category = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    author = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=256)
    promote = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=256)


# class PromoteSerializer(serializers.Serializer):
#     title = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
#     author = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=256)
#     category = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
#     cover = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=256)
#     avatar = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=256)
#     created_at = serializers.DateTimeField(required=True, allow_null=False)

class SingleArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    cover = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=256)
    content = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=2048)
    created_at = serializers.DateTimeField(required=True, allow_null=False)


class SubmitArticleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    cover = serializers.FileField(required=True, allow_null=False, allow_empty_file=False)
    content = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=2048)
    category_id = serializers.IntegerField(required=True, allow_null=False)
    author_id = serializers.IntegerField(required=True, allow_null=False)
    promote = serializers.BooleanField(required=True, allow_null=False)


class UpdateArticleCoverSerializer(serializers.Serializer):
    article_id = serializers.IntegerField(required=True, allow_null=False)
    cover = serializers.FileField(required=True, allow_null=False, allow_empty_file=False)


class DeleteArticleSerializer(serializers.Serializer):
    article_id = serializers.IntegerField(required=True, allow_null=False)

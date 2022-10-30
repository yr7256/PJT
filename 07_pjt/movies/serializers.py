from rest_framework import serializers
from .models import Movie, Actor, Review

class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name',)

class MovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)

class ActorSerializer(serializers.ModelSerializer):

    movies = MovieTitleSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)

class ActorNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name',)

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)

class MovieSerializer(serializers.ModelSerializer):

    actors = ActorNameSerializer(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):

    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
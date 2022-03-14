from django.shortcuts import render
from django.utils import timezone
from rest_framework.views import APIView, Response
from utils import status_codes

from blog.models import Post
from blog.serializers import PostSerializer


class PostView(APIView):
    def get(self, request):
        context = request.GET.get("context")
        if context == "user":
            user_id = request.GET.get("user")
            try:
                user_id = int(user_id)
            except TypeError:
                user_id = request.user.id
            posts = Post.objects.filter(user__pk=user_id)
            serializer = PostSerializer(posts, many=True)
            return Response({
                "code": status_codes.SUCCESS,
                "message": "All posts did returned.",
                "data": serializer.data
            })
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({
            "code": status_codes.SUCCESS,
            "message": "All posts did returned.",
            "data": serializer.data
        })

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "code": status_codes.SUCCESS,
                "message": "The post saved successful."
            })
        else:
            return Response({
                "code": status_codes.BAD_REQUEST,
                "message": "The post did not saved.",
                "errors": serializer.error_messages
            })

    def put(self, request):
        id = request.GET.get("id")
        try:
            post = Post.objects.get(pk=int(id))
        except Exception as ex:
            return Response({
                "code": status_codes.BAD_REQUEST,
                "message": ex.__str__()
            })
        serializer = PostSerializer(data={
            **request.data,
            "user": request.user.id
        }, instance=post)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "code": status_codes.SUCCESS,
                "message": "The post saved successful."
            })
        else:
            return Response({
                "code": status_codes.BAD_REQUEST,
                "message": "The post did not saved.",
                "errors": serializer.error_messages
            })


    def delete(self, request):
        id = request.GET.get("id")
        try:
            Post.objects.filter(pk=int(id)).delete()
        except Exception as ex:
            return Response({
                "code": status_codes.BAD_REQUEST,
                "message": ex.__str__()
            })
        return Response({
            "code": status_codes.SUCCESS,
            "message": "The post saved successful."
        })


class LikePostView():
    def put(self, request):
        id = request.GET.get("id")
        user = request.user

        try:
            id = int(id)
        except TypeError:
            return Response({
                "code": status_codes.BAD_REQUEST,
                "message": "The type of 'id' must be a string."
            })
        except Exception as ex:
            return Response({
                "code": status_codes.BAD_REQUEST,
                "message": ex.__str__()
            })

        try:
            post = Post.objects.get(pk=id)
        except Exception as ex:
            return Response({
                "code": status_codes.BAD_REQUEST,
                "message": ex.__str__()
            })

        if post.likes.filter(pk=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        
        return Response({
            "code": status_codes.SUCCESS,
            "message": "Post has been saved.",
            "data": PostSerializer(post).data
        })

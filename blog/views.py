from django.http import HttpRequest
from django.utils import timezone
from rest_framework.views import APIView, Response
from utils import status_codes

from blog.models import Post, PostComment
from blog.serializers import (PostCommentCreateSerializer,
                              PostCommentSerializer, PostCreateSerializer,
                              PostSerializer)


class PostView(APIView):
    def get(self, request: HttpRequest):
        context = request.GET.get("context")
        if context == "user":
            user_id = request.GET.get("user")
            try:
                user_id = int(user_id)
            except TypeError:
                user_id = request.user.id
            posts = Post.objects.filter(user__pk=user_id).order_by("created_time")
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

    def post(self, request: HttpRequest):
        serializer = PostCreateSerializer(data={"body": request.data, "user": request.user.id, "created_time": timezone.now()})
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

    def put(self, request: HttpRequest):
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


    def delete(self, request: HttpRequest):
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
            "message": "The post was saved successful."
        })

class PostLikeView(APIView):
    def put(self, request: HttpRequest):
        id = request.GET.get("id")

        try:
            id = int(id)
        except TypeError:
            return Response({
                "code": status_codes.BAD_REQUEST,
                "message": "The type of id should be a string."
            })
        except Exception as ex:
            return Response({
                "code": status_codes.BAD_REQUEST,
                "message": ex.__str__()
            })

        try:
            post: Post = Post.objects.get(pk=id)
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
            "message": "Post was saved successful.",
            "data": PostSerializer(post).data
        })

class PostCommentsView(APIView):
    def get(self, request: HttpRequest):
        pid = request.GET.get("pid", None)
        try:
            pid = int(pid)
        except:
            return Response({
                "code": status_codes.BAD_REQUEST,
                "message": "The type of post id should be a string.",
            })
        comments = PostComment.objects.filter(post__pk=pid)
        return Response({
            "code": status_codes.SUCCESS,
            "message": "The comments were returned.",
            "data": PostCommentSerializer(comments).data
        })

    def post(self, request: HttpRequest):
        serializer = PostCommentCreateSerializer(data={**request.data, "user": request.user.id})
        is_valid = serializer.is_valid()
        if not is_valid:
            return Response({
                "code": status_codes.BAD_REQUEST,
                "message": "Comment data is not valid.",
                "errors": serializer.errors
            })
        return Response({
            "code": status_codes.INFO,
            "message": "Successful."
        })


    def put(self, request):
        pass

    def delete(self, request):
        pass

# # myapp/serializers.py
# from rest_framework import serializers
# from .models import User
# import face_recognition
# import numpy as np

# class RegisterSerializer(serializers.ModelSerializer):
#     face_image = serializers.ImageField(write_only=True)

#     class Meta:
#         model = User
#         fields = ('username', 'password', 'face_image')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         face_image = validated_data.pop('face_image')
#         image = face_recognition.load_image_file(face_image)
#         face_encodings = face_recognition.face_encodings(image)
#         face_ = face_recognition.face_landmarks(image)
#         print(face_,'-----face')
#         print(face_encodings)
#         if not face_encodings:
#             raise serializers.ValidationError("No face found in the image.")
        
#         face_encoding = face_encodings[0]
#         user = User(
#             username=validated_data['username'],
#         )
#         user.set_password(validated_data['password'])
#         user.set_face_encoding(face_encoding)
#         user.save()
#         return user

# class LoginSerializer(serializers.Serializer):
#     face_image = serializers.ImageField()

#     def validate(self, data):
#         print(data)
#         face_image = data.get('face_image')
#         image = face_recognition.load_image_file(face_image)
#         print(image)
#         face_encodings = face_recognition.face_encodings(image)
        
#         print(face_encodings)
#         if not face_encodings:
#             raise serializers.ValidationError("No face found in the image.")
        
#         face_encoding = face_encodings[0]
#         users = User.objects.all()
#         for user in users:
#             print(user)
#             user_face_encoding = user.get_face_encoding()
#             match = face_recognition.compare_faces([user_face_encoding], face_encoding)[0]
#             if match:
#                 data['user'] = user
#                 return data
#         raise serializers.ValidationError("No matching user found.")





# myapp/serializers.py
from rest_framework import serializers
from .models import User
import face_recognition
import numpy as np

class RegisterSerializer(serializers.ModelSerializer):
    face_image = serializers.ImageField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'face_image')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        face_image = validated_data.pop('face_image')
        image = face_recognition.load_image_file(face_image)
        face_encodings = face_recognition.face_encodings(image)
        face_ = face_recognition.face_landmarks(image)
        print(face_,'-----face')
        print(face_encodings)
        if not face_encodings:
            raise serializers.ValidationError("No face found in the image.")
        
        face_encoding = face_encodings[0]
        user = User(
            username=validated_data['username'],
        )

        user.set_face_encoding(face_encoding)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    face_image = serializers.ImageField()

    def validate(self, data):
        print(data)
        face_image = data.get('face_image')
        image = face_recognition.load_image_file(face_image)
        print(image)
        face_encodings = face_recognition.face_encodings(image)
        
        print(face_encodings)
        if not face_encodings:
            raise serializers.ValidationError("No face found in the image.")
        
        face_encoding = face_encodings[0]
        users = User.objects.all()
        for user in users:
            print(user)
            user_face_encoding = user.get_face_encoding()
            match = face_recognition.compare_faces([user_face_encoding], face_encoding)[0]
            if match:
                data['user'] = user
                return data
        raise serializers.ValidationError("No matching user found.")

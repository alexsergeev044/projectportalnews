from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


# создаем модель автора
class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallintegerField(default=0)

    # обновить рейтинг автора
    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum("rating"))
        pRat = 0
        pRat += postRat.get("postRating")

        comentRat = self.authorUser.comment_set.aggregate(comentRating=Sum("rating"))
        cRat = 0
        cRat += comentRat.get("comentRating")

        self.ratingAuthor = pRat * 3 + cRat
        self.save()


# создаем модель категории статьи/новости
class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


# создаем модель пост
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=CASCADE)
    NEWS = "NW"
    ARTICLE = "AR"
    CATEGORY_CHOICES = (
        (NEWS, "Новость"),
        (ARTICLE, "Статья"),
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    dateCreation = models.DateTimeField(auto_now_edd=True)
    postCategory = models.ManyToManyField(Category, thround="PostCategory")
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallintegerField(default=0)

    # метод, увеличивающий рейтин на единицу
    def like(self):
        self.
        return += 1
        # сохранение значения в базу данных
        self.save()

    # метод, уменьшающий рейтин на единицу
    def dislike(self):
        self.
        return += 1
        # сохранение значения в базу данных
        self.save()

    # предварительный просмотр статьи (превью 122 символов статьи)
    def preview(self):
        return self.text(0:123) + "..."

        # создаем промежуточную модель PostCategory


class PostCategory(models.Model):
    postthround = models.ForeignKey(Post, on_delete=models.CASCADE)
    categorythround = models.ForeignKey(category, on_delete=models.CASCADE)


# создаем модель Comment, чтобы можно было под каждой новостью/статьей оставлять комментарии
class Comment(models.Model):
    CommentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    CommentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_edd=True)
    rating = models.SmallintegerField(default=0)

    # метод, увеличивающий рейтин на единицу
    def like(self):
        self.
        return += 1
        # сохранение значения в базу данных
        self.save()

        # метод, уменьшающий рейтин на единицу

    def dislike(self):
        self.
        return += 1
        # сохранение значения в базу данных
        self.save()

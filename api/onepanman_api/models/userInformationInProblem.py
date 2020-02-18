from django.contrib.auth.models import User
from django.db import models

from onepanman_api.models import Problem, Code


class UserInformationInProblem(models.Model):
    """
    UserInformationInProblem
    User - Problem
    """

    id = models.AutoField(
        "ID",
        db_column="ID",
        primary_key=True,
        null=False,
        blank=False,
    )

    user = models.ForeignKey(
        User,
        verbose_name="유저",
        db_column="USER",
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        related_name="user_userInformationInProblem_user",
    )

    problem = models.ForeignKey(
        Problem,
        verbose_name="문제",
        db_column="PROBLEM",
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        related_name="problem_userInformationInProblem_problem",
    )

    score = models.IntegerField(
        "점수",
        db_column="SCORE",
        null=False,
        default=0,
    )

    tier = models.CharField(
        "등급",
        db_column="TIRE",
        null=False,
        default="Bronze",
        max_length=20,
    )

    code = models.ForeignKey(
        Code,
        verbose_name="대표 코드",
        db_column="CODE",
        on_delete=models.PROTECT,
        default=0,
    )

    def __str__(self):
        return '{}문제, {}유저의 점수는 {}입니다.'.format(self.problem.title, self.user.username, self.score)

    class Meta:
        db_table = "USERINFORMATIONINPROBLEM"
        ordering = ['id', 'problem__id', 'score']
        verbose_name = "문제:유저점수정보"
        verbose_name_plural = "문제:유저점수정보"


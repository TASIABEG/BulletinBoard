from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment, Bulletin, CategoryModel
from django.contrib.sites.shortcuts import get_current_site
from .views import accepted
from django.contrib.auth.models import User  # users is sender
from django.core.mail import send_mail, EmailMultiAlternatives
from datetime import date, timedelta
from django.template.loader import render_to_string
from django.conf import settings  # Исправленный импорт настроек

@receiver(post_save, sender=Comment)
def create_comment(sender, instance, **kwargs):
    post_url = instance.get_absolute_url()
    full_url = ''.join(['http://', get_current_site('127.0.0.1').domain, ':8000']) + post_url

    auth = Comment.objects.get(id=instance.id).bulletin.author

    print(full_url)

    send_mail(
        subject=f'A new comment from "{instance.username}" is created!',
        message=f'{instance.date_added.strftime("%d %m %Y")} - {instance.body [:50]}',
        from_email='os.getenv("EMAIL")',
        recipient_list=[auth.email]
    )

@receiver(accepted)
def comment_accepted(sender, **kwargs):
    bulletin = Comment.objects.get(pk=kwargs['pk']).bulletin
    comment = Comment.objects.get(pk=kwargs['pk'])
    comment_auth = comment.username

    print(comment.body)
    print(comment_auth.email)

    send_mail(
        subject=f'Your comment is accepted!',
        message=f'Your comment in post {bulletin.title} from {comment.date_added.strftime("%d/%m/%Y")} - with content {comment.body[:50]} is accepted',
        from_email='FPW-13@yandex.ru',
        recipient_list=[comment_auth.email]
    )

def week_post():
    start = date.today() - timedelta(7)
    finish = date.today()

    list_of_bulletins = Bulletin.objects.filter(date_created__range=(start, finish))
    categories = CategoryModel.objects.all()

    for category in categories:
        subscribers_emails = []
        for user in User.objects.all():
            if user.subscriber.filter(category_name=category).exists():
                subscribers_emails.append(user.email)

        html_content = render_to_string('apscheduler/week_posts.html', {'posts': list_of_bulletins, 'category': category})

        msg = EmailMultiAlternatives(
            subject=f'По Вашей подписке появились новые объявления за прошедшую неделю',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=subscribers_emails,
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        print('Еженедельная рассылка успешна отправлена')
        print(subscribers_emails)
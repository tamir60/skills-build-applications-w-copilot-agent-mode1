from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from fitness.models import UserProfile, Activity, Team, WorkoutSuggestion

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **options):
        # Create test users
        user1, created1 = User.objects.get_or_create(
            username='alice',
            defaults={'email': 'alice@example.com', 'password': 'password123'}
        )
        if created1:
            user1.set_password('password123')
            user1.save()

        user2, created2 = User.objects.get_or_create(
            username='bob',
            defaults={'email': 'bob@example.com', 'password': 'password123'}
        )
        if created2:
            user2.set_password('password123')
            user2.save()

        user3, created3 = User.objects.get_or_create(
            username='charlie',
            defaults={'email': 'charlie@example.com', 'password': 'password123'}
        )
        if created3:
            user3.set_password('password123')
            user3.save()

        # Create profiles
        UserProfile.objects.get_or_create(
            user=user1,
            defaults={'age': 28, 'weight': 65, 'height': 170, 'fitness_goal': 'Weight loss'}
        )
        UserProfile.objects.get_or_create(
            user=user2,
            defaults={'age': 32, 'weight': 80, 'height': 180, 'fitness_goal': 'Muscle gain'}
        )
        UserProfile.objects.get_or_create(
            user=user3,
            defaults={'age': 25, 'weight': 70, 'height': 175, 'fitness_goal': 'Endurance'}
        )

        # Create activities
        Activity.objects.get_or_create(
            user=user1,
            activity_type='running',
            duration=45,
            defaults={'distance': 7.5, 'calories_burned': 400}
        )
        Activity.objects.get_or_create(
            user=user1,
            activity_type='cycling',
            duration=60,
            defaults={'distance': 20, 'calories_burned': 500}
        )
        Activity.objects.get_or_create(
            user=user2,
            activity_type='weightlifting',
            duration=90,
            defaults={'calories_burned': 300}
        )
        Activity.objects.get_or_create(
            user=user3,
            activity_type='swimming',
            duration=30,
            defaults={'distance': 1.5, 'calories_burned': 250}
        )

        # Create teams
        team1, _ = Team.objects.get_or_create(
            name='Fit Warriors',
            defaults={'description': 'A team for fitness enthusiasts'}
        )
        team1.members.set([user1, user2])
        team2, _ = Team.objects.get_or_create(
            name='Health Heroes',
            defaults={'description': 'Promoting healthy lifestyles'}
        )
        team2.members.set([user3])

        # Create suggestions
        WorkoutSuggestion.objects.get_or_create(
            user=user1,
            defaults={'suggestion': 'Try interval training for better cardio.'}
        )
        WorkoutSuggestion.objects.get_or_create(
            user=user2,
            defaults={'suggestion': 'Focus on compound lifts for muscle building.'}
        )
        WorkoutSuggestion.objects.get_or_create(
            user=user3,
            defaults={'suggestion': 'Incorporate yoga for flexibility.'}
        )

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
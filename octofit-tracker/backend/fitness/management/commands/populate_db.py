from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from fitness.models import UserProfile, Activity, Team, WorkoutSuggestion

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **options):
        # Create test users (excluding alice)
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

        # Add more test users
        user4, created4 = User.objects.get_or_create(
            username='diana',
            defaults={'email': 'diana@example.com', 'password': 'password123'}
        )
        if created4:
            user4.set_password('password123')
            user4.save()

        user5, created5 = User.objects.get_or_create(
            username='eve',
            defaults={'email': 'eve@example.com', 'password': 'password123'}
        )
        if created5:
            user5.set_password('password123')
            user5.save()

        # Create profiles
        UserProfile.objects.get_or_create(
            user=user2,
            defaults={'age': 32, 'weight': 80, 'height': 180, 'fitness_goal': 'Muscle gain'}
        )
        UserProfile.objects.get_or_create(
            user=user3,
            defaults={'age': 25, 'weight': 70, 'height': 175, 'fitness_goal': 'Endurance'}
        )
        UserProfile.objects.get_or_create(
            user=user4,
            defaults={'age': 30, 'weight': 60, 'height': 165, 'fitness_goal': 'Weight loss'}
        )
        UserProfile.objects.get_or_create(
            user=user5,
            defaults={'age': 27, 'weight': 75, 'height': 172, 'fitness_goal': 'General fitness'}
        )

        # Create activities
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
        Activity.objects.get_or_create(
            user=user4,
            activity_type='yoga',
            duration=60,
            defaults={'calories_burned': 150}
        )
        Activity.objects.get_or_create(
            user=user5,
            activity_type='running',
            duration=40,
            defaults={'distance': 6.0, 'calories_burned': 350}
        )
        # Add more activities
        Activity.objects.get_or_create(
            user=user2,
            activity_type='cycling',
            duration=75,
            defaults={'distance': 25, 'calories_burned': 450}
        )
        Activity.objects.get_or_create(
            user=user3,
            activity_type='tennis',
            duration=90,
            defaults={'calories_burned': 400}
        )
        Activity.objects.get_or_create(
            user=user4,
            activity_type='pilates',
            duration=45,
            defaults={'calories_burned': 200}
        )
        Activity.objects.get_or_create(
            user=user5,
            activity_type='basketball',
            duration=60,
            defaults={'calories_burned': 500}
        )

        # Create teams
        team1, _ = Team.objects.get_or_create(
            name='Fit Warriors',
            defaults={'description': 'A team for fitness enthusiasts'}
        )
        team1.members.set([user2, user3])
        team2, _ = Team.objects.get_or_create(
            name='Health Heroes',
            defaults={'description': 'Promoting healthy lifestyles'}
        )
        team2.members.set([user4, user5])
        team3, _ = Team.objects.get_or_create(
            name='Active Athletes',
            defaults={'description': 'For competitive sports lovers'}
        )
        team3.members.set([user2, user5])

        # Create suggestions
        WorkoutSuggestion.objects.get_or_create(
            user=user2,
            defaults={'suggestion': 'Focus on compound lifts for muscle building.'}
        )
        WorkoutSuggestion.objects.get_or_create(
            user=user3,
            defaults={'suggestion': 'Incorporate yoga for flexibility.'}
        )
        WorkoutSuggestion.objects.get_or_create(
            user=user4,
            defaults={'suggestion': 'Try HIIT workouts for efficient fat burning.'}
        )
        WorkoutSuggestion.objects.get_or_create(
            user=user5,
            defaults={'suggestion': 'Include strength training twice a week.'}
        )

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from django.contrib.auth.models import User
from fitness.models import UserProfile, Activity, Team, WorkoutSuggestion

# Create test users
user1 = User.objects.create_user('alice', 'alice@example.com', 'password123')
user2 = User.objects.create_user('bob', 'bob@example.com', 'password123')
user3 = User.objects.create_user('charlie', 'charlie@example.com', 'password123')

# Create profiles
UserProfile.objects.create(user=user1, age=28, weight=65, height=170, fitness_goal='Weight loss')
UserProfile.objects.create(user=user2, age=32, weight=80, height=180, fitness_goal='Muscle gain')
UserProfile.objects.create(user=user3, age=25, weight=70, height=175, fitness_goal='Endurance')

# Create activities
Activity.objects.create(user=user1, activity_type='running', duration=45, distance=7.5, calories_burned=400)
Activity.objects.create(user=user1, activity_type='cycling', duration=60, distance=20, calories_burned=500)
Activity.objects.create(user=user2, activity_type='weightlifting', duration=90, calories_burned=300)
Activity.objects.create(user=user3, activity_type='swimming', duration=30, distance=1.5, calories_burned=250)

# Create teams
team1 = Team.objects.create(name='Fit Warriors', description='A team for fitness enthusiasts')
team1.members.add(user1, user2)
team2 = Team.objects.create(name='Health Heroes', description='Promoting healthy lifestyles')
team2.members.add(user3)

# Create suggestions
WorkoutSuggestion.objects.create(user=user1, suggestion='Try interval training for better cardio.')
WorkoutSuggestion.objects.create(user=user2, suggestion='Focus on compound lifts for muscle building.')
WorkoutSuggestion.objects.create(user=user3, suggestion='Incorporate yoga for flexibility.')

print("Test data populated successfully!")
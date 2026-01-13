import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Card, Button } from 'react-bootstrap';
import api from '../services/api';

const Dashboard = ({ onLogout }) => {
  const [profile, setProfile] = useState(null);
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetchProfile();
    fetchActivities();
  }, []);

  const fetchProfile = async () => {
    try {
      const response = await api.get('/api/profiles/');
      if (response.data.length > 0) {
        setProfile(response.data[0]);
      }
    } catch (err) {
      console.error('Error fetching profile:', err);
    }
  };

  const fetchActivities = async () => {
    try {
      const response = await api.get('/api/activities/');
      setActivities(response.data.slice(0, 5)); // Show last 5 activities
    } catch (err) {
      console.error('Error fetching activities:', err);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    onLogout();
  };

  return (
    <Container className="mt-5">
      <Row className="mb-4">
        <Col>
          <h2>Dashboard</h2>
          <Button variant="secondary" onClick={handleLogout}>Logout</Button>
        </Col>
      </Row>
      <Row>
        <Col md={6}>
          <Card>
            <Card.Header>Profile</Card.Header>
            <Card.Body>
              {profile ? (
                <div>
                  <p><strong>Username:</strong> {profile.user.username}</p>
                  <p><strong>Age:</strong> {profile.age}</p>
                  <p><strong>Weight:</strong> {profile.weight} kg</p>
                  <p><strong>Goal:</strong> {profile.fitness_goal}</p>
                </div>
              ) : (
                <p>Loading profile...</p>
              )}
            </Card.Body>
          </Card>
        </Col>
        <Col md={6}>
          <Card>
            <Card.Header>Recent Activities</Card.Header>
            <Card.Body>
              {activities.length > 0 ? (
                activities.map(activity => (
                  <div key={activity.id} className="mb-2">
                    <strong>{activity.activity_type}</strong> - {activity.duration} min
                    {activity.distance && ` - ${activity.distance} km`}
                  </div>
                ))
              ) : (
                <p>No activities yet</p>
              )}
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default Dashboard;
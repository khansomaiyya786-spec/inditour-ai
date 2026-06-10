# MongoDB Schema — IndiTour AI

## Collections

### destinations
- _id, name, state, type, rating, description, image

### users
- _id, name, email, preference, joined_date, trips

### hotels
- _id, name, destination_id, stars, type, price

### bookings
- _id, user_id, destination_id, hotel_id, date, status
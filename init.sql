USE carsDB;

-- Create a Cars table if it doesn't exist
CREATE TABLE IF NOT EXISTS Cars (
    id INT AUTO_INCREMENT PRIMARY KEY,
    car VARCHAR(255) NOT NULL,
    carColor VARCHAR(255) NOT NULL,
    licensePlate VARCHAR(20) NOT NULL,
    num VARCHAR(20) NOT NULL,
    email VARCHAR(255) NOT NULL
);

-- Insert info into table
INSERT INTO Cars (car, carColor, licensePlate, num, email) VALUES
    ('Honda Accord 2018', 'Red', 'X2B43C', '2019823220', 'opdparkingpermit@gmail.com'),
    ('Audi S4 2013', 'Grey', 'JRE493', '2019823220', 'opdparkingpermit@gmail.com'),
    ('Toyota Sienna 2022', 'White', 'W33CDR', '2019823220', 'opdparkingpermit@gmail.com');
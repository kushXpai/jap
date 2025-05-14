class Vehicle {
    String make;
    String model;

    public Vehicle(String make, String model) {
        this.make = make;
        this.model = model;
    }

    public void display() {
        System.out.println("Vehicle: " + make + " " + model);
    }
}

class Car extends Vehicle {
    String fuelType;

    public Car(String make, String model, String fuelType) {
        super(make, model);
        this.fuelType = fuelType;
    }

    @Override
    public void display() {
        System.out.println("Car: " + make + " " + model + ", Fuel Type: " + fuelType);
    }

    public void fuelEfficiency() {
        System.out.println("Fuel efficiency data not provided.");
    }

    public void fuelEfficiency(int mileage) {
        System.out.println("Car mileage: " + mileage + " km/l");
    }
}

class Truck extends Vehicle {
    int loadCapacity;

    public Truck(String make, String model, int loadCapacity) {
        super(make, model);
        this.loadCapacity = loadCapacity;
    }

    @Override
    public void display() {
        System.out.println("Truck: " + make + " " + model + ", Load Capacity: " + loadCapacity + " tons");
    }

    public void fuelEfficiency() {
        System.out.println("Fuel efficiency data not provided.");
    }

    public void fuelEfficiency(int load) {
        System.out.println("Truck fuel efficiency for load " + load + " tons: 8 km/l");
    }
}

public class lab9oops {
    public static void main(String[] args) {
        Vehicle vehicle = new Vehicle("Generic", "Model X");
        Car car = new Car("Toyota", "Corolla", "Petrol");
        Truck truck = new Truck("Volvo", "FH", 10);

        vehicle.display();
        car.display();
        truck.display();

        car.fuelEfficiency();
        car.fuelEfficiency(15);

        truck.fuelEfficiency();
        truck.fuelEfficiency(5);
    }
}

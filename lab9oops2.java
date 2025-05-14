// Abstract class
abstract class Vehicle {
    protected String make;
    protected String model;

    public Vehicle(String make, String model) {
        this.make = make;
        this.model = model;
    }

    // Abstract methods
    public abstract void display();
    public abstract void fuelEfficiency(); // No argument
    public abstract void fuelEfficiency(double data); // Overloaded method
}

// Car class extending Vehicle
class Car extends Vehicle {
    private String fuelType;

    public Car(String make, String model, String fuelType) {
        super(make, model);
        this.fuelType = fuelType;
    }

    @Override
    public void display() {
        System.out.println("Car: " + make + " " + model + ", Fuel Type: " + fuelType);
    }

    @Override
    public void fuelEfficiency() {
        System.out.println("Fuel efficiency data not provided.");
    }

    @Override
    public void fuelEfficiency(double mileage) {
        System.out.println("Car mileage: " + mileage + " km/l");
    }
}

// Truck class extending Vehicle
class Truck extends Vehicle {
    private int loadCapacity;

    public Truck(String make, String model, int loadCapacity) {
        super(make, model);
        this.loadCapacity = loadCapacity;
    }

    @Override
    public void display() {
        System.out.println("Truck: " + make + " " + model + ", Load Capacity: " + loadCapacity + " tons");
    }

    @Override
    public void fuelEfficiency() {
        System.out.println("Fuel efficiency data not provided.");
    }

    @Override
    public void fuelEfficiency(double load) {
        System.out.println("Truck fuel efficiency for load " + load + " tons: 8 km/l");
    }
}

// Main class
public class lab9oops2 {
    public static void main(String[] args) {
        Car car = new Car("Toyota", "Corolla", "Petrol");
        Truck truck = new Truck("Volvo", "FH", 10);

        // Car details
        car.display();
        car.fuelEfficiency();
        car.fuelEfficiency(15);

        // Truck details
        truck.display();
        truck.fuelEfficiency();
        truck.fuelEfficiency(5);
    }
}

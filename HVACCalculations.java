public class HVACCalculations {

    /**
     * Calculate heating power based on flow rates and temperature differences.
     * 
     * @param flowRate Flow rate in cubic meters per second (m³/s)
     * @param deltaT Temperature difference in Kelvin (K)
     * @param specificHeat Specific heat capacity of the fluid in Joules per kilogram Kelvin (J/(kg·K))
     * @return Heating power in Watts (W)
     */
    public static double calculateHeatingPower(double flowRate, double deltaT, double specificHeat) {
        return flowRate * deltaT * specificHeat;
    }

    /**
     * Estimate cooling power based on heat extraction requirements.
     * 
     * @param heatGain Heat gain in Watts (W)
     * @return Cooling power in Watts (W)
     */
    public static double estimateCoolingPower(double heatGain) {
        return heatGain;
    }

    /**
     * Calculate pressure drop in pipes using the Darcy-Weisbach equation.
     * 
     * @param length Length of the pipe in meters (m)
     * @param diameter Diameter of the pipe in meters (m)
     * @param flowVelocity Flow velocity in meters per second (m/s)
     * @param frictionFactor Darcy friction factor (dimensionless)
     * @param density Density of the fluid in kilograms per cubic meter (kg/m³)
     * @return Pressure drop in Pascals (Pa)
     */
    public static double calculatePressureDrop(double length, double diameter, double flowVelocity, double frictionFactor, double density) {
        return (frictionFactor * length * density * Math.pow(flowVelocity, 2)) / (2 * diameter);
    }
}
# HVAC Calculations

This document provides guidelines for HVAC calculations related to heating power, cooling power estimation, and pressure drop calculations.

## Heating Power Calculation
To calculate the heating power required for a space, you can use the formula:

\[ Q = \dot{m} \times C_p \times (T_{in} - T_{out}) \]

Where:
- \( Q \) = Heating power (W)
- \( \dot{m} \) = Mass flow rate (kg/s)
- \( C_p \) = Specific heat capacity of the fluid (J/kg·K)
- \( T_{in} \) = Inlet temperature (°C)
- \( T_{out} \) = Outlet temperature (°C)

## Cooling Power Estimation
Cooling power can be estimated using the following equation:

\[ Q_c = \dot{m} \times C_p \times (T_{out} - T_{in}) \]

Where:
- \( Q_c \) = Cooling power (W)

## Pressure Drop Calculations
To calculate pressure drop in ducts or pipes, you can employ the Darcy-Weisbach equation:

\[ \Delta P = f \times \frac{L}{D} \times \frac{\rho v^2}{2} \]

Where:
- \( \Delta P \) = Pressure drop (Pa)
- \( f \) = Friction factor (dimensionless)
- \( L \) = Length of the duct or pipe (m)
- \( D \) = Diameter of the duct or pipe (m)
- \( \rho \) = Density of the fluid (kg/m³)
- \( v \) = Flow velocity (m/s)
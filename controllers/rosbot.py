from controller import Robot

# Inicializa o robô AeroShield
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Inicializa os 4 motores do chassi Rosbot
print("--- Inicializando Motores do AeroShield Robotics ---")
motor_names = ['front_left_motor', 'front_right_motor', 'rear_left_motor', 'rear_right_motor']
motors = []
for name in motor_names:
    motor = robot.getDevice(name)
    motor.setPosition(float('inf')) # Modo de velocidade contínua
    motor.setVelocity(0.0)
    motors.append(motor)

print("AeroShield pronto para patrulha!")

# Loop principal da simulação
while robot.step(timestep) != -1:
    # LÓGICA DE ROTINA: Mover para frente inspecionando a pista
    for motor in motors:
        motor.setVelocity(2.0) # Velocidade simulada das rodas
        
    print("Inspecionando área de movimento do aeródromo... Buscando FOD e Fauna.")

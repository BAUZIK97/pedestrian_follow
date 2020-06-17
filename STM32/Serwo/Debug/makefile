################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include Drivers/STM32F7xx_HAL_Driver/Src/subdir.mk
-include Core/Startup/subdir.mk
-include Core/Src/subdir.mk
-include subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 
EXECUTABLES += \
Serwo.elf \

SIZE_OUTPUT += \
default.size.stdout \

OBJDUMP_LIST += \
Serwo.list \

OBJCOPY_BIN += \
Serwo.bin \


# All Target
all: Serwo.elf secondary-outputs

# Tool invocations
Serwo.elf: $(OBJS) $(USER_OBJS) C:\Users\Marcin\STM32CubeIDE\workspace_1.0.2\Serwo\STM32F746ZGTX_FLASH.ld
	arm-none-eabi-gcc -o "Serwo.elf" @"objects.list" $(USER_OBJS) $(LIBS) -mcpu=cortex-m7 -T"C:\Users\Marcin\STM32CubeIDE\workspace_1.0.2\Serwo\STM32F746ZGTX_FLASH.ld" --specs=nosys.specs -Wl,-Map="Serwo.map" -Wl,--gc-sections -static --specs=nano.specs -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -Wl,--start-group -lc -lm -Wl,--end-group
	@echo 'Finished building target: $@'
	@echo ' '

default.size.stdout: $(EXECUTABLES)
	arm-none-eabi-size  $(EXECUTABLES)
	@echo 'Finished building: $@'
	@echo ' '

Serwo.list: $(EXECUTABLES)
	arm-none-eabi-objdump -h -S $(EXECUTABLES) > "Serwo.list"
	@echo 'Finished building: $@'
	@echo ' '

Serwo.bin: $(EXECUTABLES)
	arm-none-eabi-objcopy  -O binary $(EXECUTABLES) "Serwo.bin"
	@echo 'Finished building: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) *
	-@echo ' '

secondary-outputs: $(SIZE_OUTPUT) $(OBJDUMP_LIST) $(OBJCOPY_BIN)

.PHONY: all clean dependents
.SECONDARY:

-include ../makefile.targets

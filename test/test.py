# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # -------------------------------------------------
    # Reset
    # -------------------------------------------------
    dut._log.info("Reset")

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    # Wait for 10 clock cycles during reset
    await ClockCycles(dut.clk, 10)

    # Release reset
    dut.rst_n.value = 1

    # -------------------------------------------------
    # Test 1: 20 + 30 = 50
    # -------------------------------------------------
    dut._log.info("Test 1: 20 + 30")

    dut.ui_in.value = 20
    dut.uio_in.value = 30

    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value == 50

    # -------------------------------------------------
    # Test 2: 10 + 5 = 15
    # -------------------------------------------------
    dut._log.info("Test 2: 10 + 5")

    dut.ui_in.value = 10
    dut.uio_in.value = 5

    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value == 15

    # -------------------------------------------------
    # Test 3: 100 + 50 = 150
    # -------------------------------------------------
    dut._log.info("Test 3: 100 + 50")

    dut.ui_in.value = 100
    dut.uio_in.value = 50

    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value == 150

    # -------------------------------------------------
    # Test 4: 0 + 0 = 0
    # -------------------------------------------------
    dut._log.info("Test 4: 0 + 0")

    dut.ui_in.value = 0
    dut.uio_in.value = 0

    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value == 0

    # -------------------------------------------------
    # Test 5: 255 + 0 = 255
    # -------------------------------------------------
    dut._log.info("Test 5: 255 + 0")

    dut.ui_in.value = 255
    dut.uio_in.value = 0

    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value == 255

    # -------------------------------------------------
    # Test 6: 100 + 100 = 200
    # -------------------------------------------------
    dut._log.info("Test 6: 100 + 100")

    dut.ui_in.value = 100
    dut.uio_in.value = 100

    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value == 200

    # -------------------------------------------------
    # Test 7: Overflow test
    # 255 + 1 = 256
    # Since output is 8-bit, expected result = 0
    # -------------------------------------------------
    dut._log.info("Test 7: 255 + 1 (overflow)")

    dut.ui_in.value = 255
    dut.uio_in.value = 1

    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value == 0

    # -------------------------------------------------
    # Test 8: 200 + 55 = 255
    # -------------------------------------------------
    dut._log.info("Test 8: 200 + 55")

    dut.ui_in.value = 200
    dut.uio_in.value = 55

    await ClockCycles(dut.clk, 1)

    assert dut.uo_out.value == 255

    # -------------------------------------------------
    # Test completed
    # -------------------------------------------------
    dut._log.info("All tests passed!")

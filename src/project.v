/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_example (
    input  wire [7:0] ui_in,       // Dedicated inputs
    output wire [7:0] uo_out,      // Dedicated outputs
    input  wire [7:0] uio_in,      // IOs: Input path
    output wire [7:0] uio_out,     // IOs: Output path
    output wire [7:0] uio_oe,      // IOs: Enable path
                                  // 0 = input, 1 = output
    input  wire       ena,         // Enable
    input  wire       clk,         // Clock
    input  wire       rst_n        // Active-low reset
);

    // -------------------------------------------------
    // Main logic
    // Adds the two 8-bit input values
    // -------------------------------------------------
    assign uo_out = ui_in + uio_in;

    // -------------------------------------------------
    // Unused bidirectional IO outputs
    // -------------------------------------------------
    assign uio_out = 8'b00000000;

    // Set all IO enable bits to 0
    // This means all uio pins are configured as inputs
    assign uio_oe = 8'b00000000;

    // -------------------------------------------------
    // Prevent unused-input warnings
    // -------------------------------------------------
    wire _unused = &{ena, clk, rst_n, 1'b0};

endmodule

`default_nettype wire

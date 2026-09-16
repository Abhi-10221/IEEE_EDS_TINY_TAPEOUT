`default_nettype none
`timescale 1ns / 1ps

/*
 * Tiny Tapeout Testbench
 *
 * This testbench instantiates the user project and provides
 * signals that can be driven and monitored by Cocotb.
 */

module tb ();

  // --------------------------------------------------
  // Clock, reset, enable and I/O signals
  // --------------------------------------------------

  reg        clk;
  reg        rst_n;
  reg        ena;

  reg  [7:0] ui_in;
  reg  [7:0] uio_in;

  wire [7:0] uo_out;
  wire [7:0] uio_out;
  wire [7:0] uio_oe;


  // --------------------------------------------------
  // Power signals for Gate-Level simulation
  // --------------------------------------------------

`ifdef GL_TEST
  wire VPWR = 1'b1;
  wire VGND = 1'b0;
`endif


  // --------------------------------------------------
  // Dump waveforms
  // --------------------------------------------------

  initial begin
    $dumpfile("tb.fst");
    $dumpvars(0, tb);
  end


  // --------------------------------------------------
  // Instantiate the user project
  // --------------------------------------------------

  tt_um_example user_project (

`ifdef GL_TEST
    .VPWR  (VPWR),
    .VGND  (VGND),
`endif

    .ui_in   (ui_in),
    .uo_out  (uo_out),

    .uio_in  (uio_in),
    .uio_out (uio_out),
    .uio_oe  (uio_oe),

    .ena     (ena),
    .clk     (clk),
    .rst_n   (rst_n)
  );


endmodule

`default_nettype wire

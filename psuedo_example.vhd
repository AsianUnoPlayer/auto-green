library IEEE;
use IEEE.STD.LOGIC.1164.ALL;
use IEEE.STD.LOGIC.ARITH.ALL;
use IEEE.STD.LOGIC.UNSIGNED.ALL;

entity vVGAmod is
    PORT(
        nRST:       in std_logic := '0';    --negative level reset
        PixelClk:   in std_logic;           --33MHz pixel clock for LCD

        -- Control
        LCD_DE:     out std_logic;          --Display Enable, high during valid pixels
        LCD_HSYNC:  out std_logic;          --Horizontal Sync [not required]
        LCD_VSYNC:  out std_logic;          --Vertical Sync [not required]

        -- Data
        LCD_R:      out std_logic_vector(7, downto 0);
        LCD_G:      out std_logic_vector(7, downto 0);
        LCD_B:      out std_logic_vector(7, downto 0)
    );
END vVGAmod;

architecture behave of vVGAmod is

signal h_pix_cntr   :   unsigned(15 downto 0);
signal v_pix_cntr   :   unsigned(15 downto 0);

signal h_pixel_count    :   unsigned(15 downto 0); --actual Horizontal pixels 0 --> 799
signal v_pix_count  :   unsigned(15 downto 0); --actual vertical pixels 0 --> 479

constant v_back_porch   :   natural := 0; --something with Vertical Back Porch
constant v_pulseW   :   natural := 5; --pulse width
constant v_displayH :   natural := 400; --Vertical Display Pixels
constant v_front_porch  :   natural := 45; --Vertical Front Porch

constant h_back_porch   :   natural := 182; --something
constant h_pulseW   :   natural := 1; --Hsync pulse width
constant h_displayW :   natural := 800; --Horizontal Display Pixels
constant h_front_porch  :   natural := 210; --Horizontal Front Porch

constant h_runLimit :   natural := h_displayW + h_back_porch + h_front_porch; -- 800 + 182 + 210 = ~1192
constant v_runLimit :   natural := v_displayH + v_back_porch + v_front_porch; -- 480 + 0 + 45 = ~525

-- original timing:
-- HSYNC=0 on H_pixCntr in [H_PulseW=1,H_DisplayW + H_BackPorch=982]
-- VSYNC=0 on V_pixCntr in [V_PulseW=5,V_runLimit-0=545]
-- DE=1 on H_pixCntr in [H_BackPorch=182,H_runLimit-H_FrontPorch=982]
--      and V_pixCntr in [V_BackPorch=0,V_runLimit-V_FrontPorch-1=479]  

begin   -- architecture behave of vVGAmod

myPixels: process (PixelClk)
    begin
        if (nRST = '0')
            then
            v_pix_cntr  <=  (others=> '0');
            h_pix_cntr  <=  (others=> '0');

        elsif (h_pix_cntr = h_runLimit)
            then
            h_pix_cntr  <=  (others=> '0');
            v_pix_cntr  <=  v_pix_cntr + 1;

        elsif (v_pix_cntr = v_runLimit)
            then
            v_pix_cntr  <=  (others=> '0');
            h_pix_cntr  <=  (others=> '0');

        else
            h_pix_cntr  <=  h_pix_cntr + 1;
        end if;
    end if;
            end process myPixels; -- Process (PixelClocks)
                
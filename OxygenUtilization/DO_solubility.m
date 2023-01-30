   
%  Input parameters Temperature [C], Salinity [permil]
   TEMP = 20.0 ; 
   SALT =  0.2 ;

% ;-----------------------------------------------------------------------
% ;     Computes oxygen saturation concentration at 1 atm total pressure
% ;     in mol/m^3 given the temperature (t, in deg C) and the salinity (s,
% ;     in permil).
% ;
% ;     FROM GARCIA AND GORDON (1992), LIMNOLOGY and OCEANOGRAPHY.
% ;     THE FORMULA USED IS FROM PAGE 1310, EQUATION (8).
% ; 	  WRITEN BY: KSCHRODER
% ;
% ;     *** NOTE: THE "A_3*TS^2" TERM (IN THE PAPER) IS INCORRECT. ***
% ;     *** IT SHOULDN'T BE THERE.                                ***
% ;
% ;     O2SAT IS DEFINED BETWEEN T(freezing) <= T <= 40(deg C) AND
% ;     O2SAT IS DEFINED BETWEEN T(freezing) <= T <= 40(deg C) AND
% ;     0 permil <= S <= 42 permil
% ;     CHECK VALUE:  T = 10.0 deg C, S = 35.0 permil,
% ;     O2SAT = 282.015 mmol/m^3
% ;-----------------------------------------------------------------------

      T0_Kelvin = 273.15 ;

% ;  TEMP    ; sea surface temperature (C)
% ;  SALT    ; sea surface salinity (psu)

% ;-----------------------------------------------------------------------
% ;     coefficients in expansion
% ;-----------------------------------------------------------------------

      a_0 = 2.00907  ;
      a_1 = 3.22014  ;
      a_2 = 4.05010  ;
      a_3 = 4.94457  ;
      a_4 = -2.56847E-1 ;
      a_5 = 3.88767 ;
      b_0 = -6.24523E-3 ;
      b_1 = -7.37614E-3 ;
      b_2 = -1.03410E-2 ;
      b_3 = -8.17083E-3 ;
      c_0 = -4.88682E-7 ;

% ;-----------------------------------------------------------------------

      TS = log( ((T0_Kelvin + 25.0) - TEMP) / (T0_Kelvin + TEMP) ) ;
      oxyarg=a_0+TS*(a_1+TS*(a_2+TS*(a_3+TS*(a_4+TS*a_5))))+SALT*(b_0+TS*(b_1+TS*(b_2+TS*b_3))+SALT*c_0) ;

      O2SAT = exp(oxyarg) ;
      
%;-----------------------------------------------------------------------
%;     Convert from ml/l to mg/L
%;-----------------------------------------------------------------------

      O2SAT = O2SAT/0.7 ;

%;-----------------------------------------------------------------------
      
      
      formatSpec = 'DO Solubility is %6.3f mg/L \n';

      fprintf(formatSpec,O2SAT)
  
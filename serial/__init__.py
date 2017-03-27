# -*- coding: utf-8 -*-

import os,sys
import serial #for port opening
import sys #for exceptions
import time
#from app import config

class Serial: 
    def __init__(self, port=None, baudrate=None, timeout=20,stopbits=None,bytesize=None,parity=None,waiting=False):
        ''' Serial connection with pyserial
        :input: port,baudrate,timeout
        :output: connection
        '''
        try:
            if waiting is False:
                self.port = serial.Serial(port = port, baudrate=baudrate, 
                timeout=timeout, writeTimeout=timeout,stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE)
            else:
                self.port = serial.Serial(port = port, baudrate=baudrate, 
                timeout=timeout, writeTimeout=timeout,stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE)
                self.port.in_waiting
        except Exception as e:
            self.error = e
            self.port = None

    def open(self): 
        ''' Open the serial port.'''
        if self.port = None:
            return self.error
        self.port.open()

    def close(self): 
        ''' Close the serial port.'''
        if self.port = None:
            return self.error
        self.port.close() 

    def send(self, msg):
        ''' Send message to serial port '''
        if self.port = None:
            return self.error
        self.port.write(msg)

    def recv(self,numberline=None):
        ''' Receive message from serial port '''
        if self.port = None:
            return self.error
    	if numberline is None:
	        return self.port.readline()
        else:
	        return self.port.read(numberline)

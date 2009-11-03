#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2009, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of the Willow Garage nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

##\author Kevin Watts

##\brief Publishes diagnostic messages for robot monitor regression test

PKG = 'runtime_monitor'

import roslib; roslib.load_manifest(PKG)

import rospy
from time import sleep

from diagnostic_msgs.msg import DiagnosticArray, DiagnosticStatus

if __name__ == '__main__':
    rospy.init_node('diag_pub')
    pub = rospy.Publisher('/diagnostics', DiagnosticArray)
    
    array = DiagnosticArray()
    array.status = [
        DiagnosticStatus(0, 'EtherCAT Device (fl_caster_l_wheel_motor)', 'OK', '', []),
        DiagnosticStatus(1, 'EtherCAT Device (fl_caster_r_wheel_motor)', 'Warning', '', []),
        DiagnosticStatus(0, 'EtherCAT Device (fl_caster_rotation_motor)', 'OK', '', []),
        DiagnosticStatus(0, 'EtherCAT Device (fr_caster_l_wheel_motor)', 'OK', '', []),
        DiagnosticStatus(2, 'EtherCAT Device (fr_caster_r_wheel_motor)', 'Error', '', []),
        DiagnosticStatus(0, 'EtherCAT Device (fr_caster_rotation_motor)', 'OK', '', []),

        DiagnosticStatus(2, 'tilt_hokuyo_node: Frequency Status', 'Error', '', []),
        DiagnosticStatus(2, 'tilt_hokuyo_node: Connection Status', 'Error', '', []),
        DiagnosticStatus(0, 'base_hokuyo_node: Frequency Status', 'OK', '', []),
        DiagnosticStatus(0, 'base_hokuyo_node: Connection Status', 'OK', '', []),

        DiagnosticStatus(0, 'Joint (fl_caster_l_wheel_joint)', 'OK', '', []),
        DiagnosticStatus(0, 'Joint (fl_caster_r_wheel_joint)', 'OK', '', []),
        DiagnosticStatus(0, 'Joint (fl_caster_rotation_joint)', 'OK', '', []),
        DiagnosticStatus(0, 'Joint (fr_caster_l_wheel_joint)', 'OK', '', []),
        DiagnosticStatus(0, 'Joint (fr_caster_r_wheel_joint)', 'OK', '', []),
        DiagnosticStatus(0, 'Joint (fr_caster_rotation_joint)', 'OK', '', [])]

    while not rospy.is_shutdown():
        pub.publish(array)
        sleep(1)

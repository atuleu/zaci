.. VerTIGo - replacing the dispenser wheel

.. |break| image:: spacer.png
   :width: 100 %
   :height: 1px


*****************************
Replacing the Dispenser Wheel
*****************************

This guide shows you how to replace the dispenser wheel on VerTIGo. The wheel
may need to be replaced if:

* Another is needed to avoid repetitive jamming of the dispenser
* The part is broken.
* The dispenser should be cleaned because some light sensor are obstructed with
  corn dust.


Tools needed
============

.. image:: screwdriver_pz1_pz2.png
   :width: 50 %
   :align: right

For this operation, a PZ1 screw driver is mostly needed as almost all screws are
M3 size. However some screw of the pellet dispenser are M4 size, and a PZ2
driver is needed.

Optionally, a magnetic screw holder could be used to help
holding / removing the screws.

You will also need some tape to hold the screen protection.

|break|

Steps
=====

0. Protect the screen
---------------------

.. image:: screen_protection.png
   :width: 50 %
   :align: right


The very first step is to protect the screen, as it is very easy to scratch it
while opening VerTIGo. For this purpose, use the screen cutout ant tape it on
the four side.

.. caution::

   The gluing of the screen is the most difficult operation whilea
   building VerTIGo, and therefore it is the most difficult part to replace.

|break|

.. _whl removing the feet:

1. Removing the back feet
--------------------------

.. image:: feet_side.png
   :width: 50 %
   :align: right

.. image:: feet_bottom.png
   :width: 50 %
   :align: right

1. Place VerTIGo upside down, on the edge of a table, the back side facing you.
2. Remove the two M3 x 8mm countersunk screws on the side of the back feet ( facing you ).
3. Remove the four M3 x 8mm pan head screws on the bottom of the back feet.
4. You can now remove the back feet


|break|


2. Opening the back panel
-------------------------

.. image:: side_screws.png
   :width: 50 %
   :align: right

1. Place Vertigo face down on the table.
2. Remove the side panels M3 x 8mm countersunk screws attached to the back panel (see photo). There are two on each sides.

|break|

.. image:: back_screws.png
   :width: 50 %
   :align: right


3. Remove the four M3 x 8mm screw holding the back panel.

4. You can now remove the backpanel by sliding up and slightly in front ( to disengage the dispenser plastic hose).

|break|

.. image:: back_connectors.png
   :width: 50 %
   :align: right


5. Remove the two cables attached to the pellet dispenser ( one USB cable, and one power cable).


|break|

.. _dissasembling pellet:

3. Dissasembling the Pellet Dispenser
-------------------------------------

.. image:: dispenser_connector_and_screws.png
   :width: 50 %
   :align: right


1. Detach the wheel optical index sensor cable.

2. Remove the four M4 x 20 mm screws holding the bottom part of the dispenser.

   .. note::

      You should use the PZ2 driver for these screws.

|break|

.. image:: dispenser_wheel_screws.png
   :width: 50 %
   :align: right


3. To Remove the wheel, remove the two M3 x 12 mm Pan Head screws holding the
   wheel.

|break|



4. Re-assembling the pellet dispenser
-------------------------------------



1. Mount the new pellet dispenser wheel to the motor shaft using the two M3 x
   12mm Pan Head screws.

   .. important::

      If you are using a connical dispensing wheel, the hole on the top side are
      smaller than the bottom side. This is to ensure a downward pressure to
      avoid jamming. Please double check the orientation of the wheel.

2. Mount the bottom part of the dispenser with the top part using the four M4 screw.

   .. note::

      You should use the PZ2 driver for these screws.


3. Put back the optical sensor cable.

   .. important::

      If not connected, the pellet dispenser won't dispense at all and always
      return "self-check test error".

|break|


5. Remounting the back panel
----------------------------


1. Plug back the USB and power connector to the pellet dispenser.

   .. note::

      Those cables are connected to the raspberry pi.

2. Slide the back panel in place. The pellet dispenser output hose does not
   align perfectly. You must guide it gently with your fingers through the front
   dispenser area.

.. image:: back_bottom_aligned.png
   :width: 50 %
   :align: right

3. Align the **bottom** of the back plate in place. Make sure the bottom plate
   (with the PC fan) slide inside the aluminium extrusion. It is normal that the
   backplate does not align fully yet as other part cannot slide in place due to
   their own weight. We will align them in a later step.

4. To help the bottom of the backplate to remain in position, screw the two
   bottom M3 x 8mm Pan Head screws in place. **Do not tie them fully yet.**

   .. note::

      As shown in the left picture the top part of the back plate remains not
      fully engaged.

|break|

.. image:: battery_module_unaligned.png
   :width: 50 %
   :align: right

.. image:: battery_module_aligned.png
   :width: 50 %
   :align: right


5. Align the battery module by pushing it gently to the side.

|break|

6. Do the same alignement on the compute module ( left side ).

.. image:: compute_module_unaligned.png
   :width: 50 %
   :align: right

.. image:: compute_module_aligned.png
   :width: 50 %
   :align: right

|break|

.. image:: back_plate_right_screws.png
   :width: 50 %
   :align: right

.. image:: back_plate_left_screws.png
   :width: 50 %
   :align: right


7. Now the back panel should be fully engaged (see right pictures). You can
   screw back the following screws:

   a. 2x M3 x 8mm Pan Head screws
   b. 4x M3 x 8mm Countersunk screws

8. Tie fully the bottom screws of the backplate.

|break|


6. Remounting the feet
-----------------------

Follow the steps in :ref:`section 1<whl removing the feet>` in reverse order.

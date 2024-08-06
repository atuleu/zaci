.. VerTIGo - replacing battery guide

.. |break| image:: spacer.png
   :width: 100 %
   :height: 1px


*********************
Replacing the Battery
*********************

This guide shows you how to replace the battery on VerTIGo.

.. important::
   This operation is mostly needed for transport, as by FAA regulation, the LiPo battery must **only** be transported in carry on luggage.


Tools needed
============

.. image:: screwdriver_pz1.png
   :width: 50 %
   :align: right

For this operation, only a PZ1 screw driver is needed as all screw are M3
size. Optionally, a magnetic screw holder could be used to help holding /
removing the screws.

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

.. _removing the feet:

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

.. _removing right panel:

3. Removing the right panel
---------------------------

.. image:: side_battery.png
   :width: 50 %
   :align: right


As the battery module is hard to get out, it is preferable to remove the right
panel ( on your left if the screen is laying on the table), to ease the access
to the battery module. For that purpose:

1. Remove the two side M3 x 8mm countersunk screw on the side.
2. Remove the two M3 x 8mm Pan Head screw on the front.

|break|


.. _removing battery:

4. Removing the battery module
------------------------------

.. image:: battery_module_connectors.png
   :width: 50 %
   :align: right


1. Disconnect the following connectors on the Battery Management System (BMS)
   board.

   a. Output Power
   b. On/Off button
   c. RPi On/Off signal
   d. Input Power
   e. USB Connector

|break|

.. image:: battery_module_screws.png
   :width: 50 %
   :align: right


2. Unscrew the two M3 x 6mm Pan Head screws holding the battery module to the
   main frame.
3. You can now slide out the battery module.

|break|

5. Removing the battery from the battery module.
------------------------------------------------

.. image:: battery_connectors.png
   :width: 50 %
   :align: right


1. Disconnect the LiPo battery from the BMS board. Please follow this order.

   a. Disconnect the main power cable
   b. Disconnect the balancing cable.

   .. note::

      To help remove the battery, you may also unplug the other cables. It is
      safe to do so if the other battery cables are removed first. All
      connectors are unique in shape, so you cannot mix them if you carefully
      replace them.


|break|

.. image:: battery_holder.png
   :width: 50 %
   :align: right



2. Unscrew the cariage screw of the battery holder.

   .. note::

      You do not need to fully remove the screw. Untie them to allow the
      holder to slide open easily. It will simplify re-assembly.

3. Push the battery holder to the side to be able to disengage the battery.


|break|

6. Install the new battery
--------------------------
|break|

.. image:: battery_cables.png
   :width: 50 %
   :align: right


1. While the battery holder are open, carefully slide the battery cables through the top
   holder ( the one with the red Printed Circuit Board).


|break|

.. image:: battery_holder_closed.png
   :width: 50 %
   :align: right

2. Close the two battery holders and tie the bottom screws. The battery should
   not be centered on the battery module: the top holder should be fully pushed,
   as shown on the left photo.

|break|

3. Connect back the battery cable in the following order:

   a. If you removed any cable connected to the BMS, plug them first.
   b. Plug the balancing cable first (5 cable connector)
   c. Plug the main power cable last.

7. Remount the battery module
-----------------------------

1. Follow the steps in :ref:`section 4 <removing battery>` in reverse order.

2. Double check that the 5 cables are connected:

   a. Output Power (Red and black)
   b. On/Off button (Polarity doesn't count)
   c. RPi On/Off signal (Polarity doesn't count)
   d. Input Power (Yellow and Black)
   e. USB Connector

   .. note::

      The On/Off button and the RPi On/Off signal are differentiated with a painted blue
      marks on the On/Off button connector and plug.

8. Remount the side panel
-------------------------

Follow the steps in :ref:`section 3<removing right panel>` in reverse order.


9. Remount the back panel
-------------------------


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


10. Remount the feet
--------------------

Follow the steps in :ref:`section 1<removing the feet>` in reverse order.

#ZEUS- I START FROM THRE, WHERE EVERYONE GIVE-UP

import zeuspy


class Update:
    def stop_propagation(self):
        raise zeuspy.StopPropagation

    def continue_propagation(self):
        raise zeuspy.ContinuePropagation

class Paper:
    def __init__(self, iso_code: str, x: int, y: int, units: str):
        self.iso_code = iso_code
        self.x = x
        self.y = y
        self.units = units


ISO_4A0 = Paper('4A0', 1682, 2378, 'mm')
ISO_2A0 = Paper('2A0', 1189, 1682, 'mm')
ISO_A0 = Paper('A0', 841, 1189, 'mm')
ISO_A1 = Paper('A1', 594, 841, 'mm')
ISO_A2 = Paper('A2', 420, 594, 'mm')
ISO_A3 = Paper('A3', 297, 420, 'mm')
ISO_A4 = Paper('A4', 210, 297, 'mm')
ISO_A5 = Paper('A5', 148, 210, 'mm')
ISO_A6 = Paper('A6', 105, 148, 'mm')
ISO_A7 = Paper('A7', 74, 105, 'mm')
ISO_A8 = Paper('A8', 52, 74, 'mm')
ISO_A9 = Paper('A9', 37, 52, 'mm')
ISO_A10 = Paper('A10', 26, 37, 'mm')

ISO_B0 = Paper('B0', 1000, 1414, 'mm')
ISO_B1 = Paper('B1', 707, 1000, 'mm')
ISO_B2 = Paper('B2', 500, 707, 'mm')
ISO_B3 = Paper('B3', 353, 500, 'mm')
ISO_B4 = Paper('B4', 250, 352, 'mm')
ISO_B5 = Paper('B5', 176, 250, 'mm')
ISO_B6 = Paper('B6', 125, 176, 'mm')
ISO_B7 = Paper('B7', 88, 125, 'mm')
ISO_B8 = Paper('B8', 62, 88, 'mm')
ISO_B9 = Paper('B9', 44, 62, 'mm')
ISO_B10 = Paper('B10', 31, 44, 'mm')

C0 = Paper('C0', 917, 1297, 'mm')
C1 = Paper('C1', 648, 917, 'mm')
C2 = Paper('C2', 458, 648, 'mm')
C3 = Paper('C3', 324, 458, 'mm')
C4 = Paper('C4', 229, 324, 'mm')
C5 = Paper('C5', 162, 229, 'mm')
C6 = Paper('C6', 114, 162, 'mm')
C7 = Paper('C7', 81, 114, 'mm')
C8 = Paper('C8', 57, 81, 'mm')
C9 = Paper('C9', 40, 57, 'mm')
C10 = Paper('C10', 28, 40, 'mm')

ISO_A2EXTRA = Paper('A2EXTRA', 445, 619, 'mm')
ISO_A3EXTRA = Paper('A3EXTRA', 322, 445, 'mm')
ISO_A3SUPER = Paper('A3SUPER', 305, 508, 'mm')
ISO_SUPERA3 = Paper('SUPERA3', 305, 487, 'mm')
ISO_A4EXTRA = Paper('A4EXTRA', 235, 322, 'mm')
ISO_A4SUPER = Paper('A4SUPER', 229, 322, 'mm')
ISO_SUPERA4 = Paper('SUPERA4', 227, 356, 'mm')
ISO_A4LONG = Paper('A4LONG', 210, 348, 'mm')
ISO_A5EXTRA = Paper('A5EXTRA', 173, 235, 'mm')
ISO_SOB5EXTRA = Paper('SOB5EXTRA', 202, 276, 'mm')

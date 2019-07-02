class Solution:
    def reverse(self, x: int) -> int:
        strX = str(x)
        if len(strX) > 0:
            if (strX[0] == "-"):
                strwithouhtminux = strX[1:]
                strwithouhtminux = strwithouhtminux[::-1]
                while (strwithouhtminux[0] == "0"):
                    strwithouhtminux = strwithouhtminux[1:]
                x = int("-" + strwithouhtminux)
            elif (strX == "0"):
                return 0
            else:
                strwithouhtminux = strX[::-1]

                while (strwithouhtminux[0] == "0"):
                    strwithouhtminux = strwithouhtminux[1:]
                x = int(strwithouhtminux)
        if (x > 2147483648 or x < -2147483648):
            return 0
        else:
            return x
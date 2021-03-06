import bitcoin


class ECDSA:
    """
    ECDSA class
    """

    @classmethod
    def sign(cls, message, private_key):
        """
        Args:
            message (string): message to sign
            private_key (string): private_key
        """

        v, r, s = bitcoin.ecdsa_raw_sign(message.encode(),
                                         private_key.encode())

        return [v, r, s]

    @classmethod
    def recover(cls, message, vrs):
        """
        Args:
            message (string): message
            vrs (tuple): tuple of v, r, s (r, s in hex)
        """

        # Convert r, s from hex to int.
        rd = int(vrs[1], 16)
        sd = int(vrs[2], 16)

        # Get raw recover of public key.
        pub_key_raw = bitcoin.ecdsa_raw_recover(message, (vrs[0], rd, sd))
        # Get x, y of public key and remove 0x from beginning.
        x = hex(pub_key_raw[0]).replace('0x', '')
        y = hex(pub_key_raw[1]).replace('0x', '')

        return x + y

from xml.dom import minidom
import argparse

# Master UIDs take from
# https://android.googlesource.com/platform/system/core/+/master/include/private/android_filesystem_config.h
androidMasterIds = {
    "0": "AID_ROOT",
    "1000": "AID_SYSTEM",
    "1001": "AID_RADIO",
    "1002": "AID_BLUETOOTH",
    "1003": "AID_GRAPHICS",
    "1004": "AID_INPUT",
    "1005": "AID_AUDIO",
    "1006": "AID_CAMERA",
    "1007": "AID_LOG",
    "1008": "AID_COMPASS",
    "1009": "AID_MOUNT",
    "1010": "AID_WIFI",
    "1011": "AID_ADB",
    "1012": "AID_INSTALL",
    "1013": "AID_MEDIA",
    "1014": "AID_DHCP",
    "1015": "AID_SDCARD_RW",
    "1016": "AID_VPN",
    "1017": "AID_KEYSTORE",
    "2000": "AID_SHELL",
    "2001": "AID_CACHE",
    "2002": "AID_DIAG",
    "3001": "AID_NET_BT_ADMIN",
    "3002": "AID_NET_BT",
    "3003": "AID_INET",
    "3004": "AID_NET_RAW",
    "3005": "AID_NET_ADMIN",
    "9998": "AID_MISC",
    "9999": "AID_NOBODY",
    "10000": "AID_APP",
}


def retrieveElem(ap, attr):
    try:
        return ap.attributes[attr].value
    except StandardError:
        return "*"


def main():
    # parse command line arguments for the packages.xml input file
    # and the output destination
    parser = argparse.ArgumentParser(description='Creates passwd file for an Android device based on its packages.xml file.')
    parser.add_argument('-i', type=str, nargs='?',
                        help='Packages.xml file\'s path.',
                        default='packages.xml')

    parser.add_argument('-o', type=str, nargs='?',
                        help='Output destination path of passwd file produced.',
                        default='android-passwd')

    try:
        fpaths = parser.parse_args()
    except IOError:
        print "Somaething went wrong while parsing command line arguments.."

    xmldoc = minidom.parse(fpaths.i)
    itemlist = xmldoc.getElementsByTagName('package')

    # passwd format -> name:x:userId::name:codePath::
    # if any element is missing or cannot be retrieved, put "" in its position
    with open(fpaths.o, 'w') as outf:
        for ap in itemlist:
            outf.write(
                retrieveElem(ap, 'name') + ":*:" +
                retrieveElem(ap, 'userId') + "::" +
                retrieveElem(ap, 'name') + ":" +
                retrieveElem(ap, 'codePath') + ":*\n"
            )

        for uid, name in androidMasterIds.items():
            outf.write(
                name + ":*:" + uid + "::" + name + ":*:*\n"
            )

if __name__ == "__main__":
    main()

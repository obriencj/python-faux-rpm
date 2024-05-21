# This library is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this library; if not, see <http://www.gnu.org/licenses/>.


"""
Faux RPM -- lookalike rpm package which does nothing

:author: Christopher O'Brien <obriencj@preoccupied.net>
:license: GPL v3
"""


from typing import Any, Dict


HEADERCONV_COMPRESSFILELIST: int = 1
HEADERCONV_EXPANDFILELIST: int = 0
HEADERCONV_RETROFIT_V3: int = 2
RPMBUILD_BUILD: int = 2
RPMBUILD_CHECK: int = 8
RPMBUILD_CLEAN: int = 16
RPMBUILD_FILECHECK: int = 32
RPMBUILD_INSTALL: int = 4
RPMBUILD_ISICON: int = 4
RPMBUILD_ISNO: int = 8
RPMBUILD_ISPATCH: int = 2
RPMBUILD_ISSOURCE: int = 1
RPMBUILD_NONE: int = 0
RPMBUILD_PACKAGEBINARY: int = 128
RPMBUILD_PACKAGESOURCE: int = 64
RPMBUILD_PKG_NODIRTOKENS: int = 1
RPMBUILD_PKG_NONE: int = 0
RPMBUILD_PREP: int = 1
RPMBUILD_RMBUILD: int = 512
RPMBUILD_RMSOURCE: int = 256
RPMBUILD_RMSPEC: int = 2048
RPMCALLBACK_CPIO_ERROR: int = 16384
RPMCALLBACK_ELEM_PROGRESS: int = 524288
RPMCALLBACK_INST_CLOSE_FILE: int = 8
RPMCALLBACK_INST_OPEN_FILE: int = 4
RPMCALLBACK_INST_PROGRESS: int = 1
RPMCALLBACK_INST_START: int = 2
RPMCALLBACK_INST_STOP: int = 262144
RPMCALLBACK_REPACKAGE_PROGRESS: int = 1024
RPMCALLBACK_REPACKAGE_START: int = 2048
RPMCALLBACK_REPACKAGE_STOP: int = 4096
RPMCALLBACK_SCRIPT_ERROR: int = 32768
RPMCALLBACK_SCRIPT_START: int = 65536
RPMCALLBACK_SCRIPT_STOP: int = 131072
RPMCALLBACK_TRANS_PROGRESS: int = 16
RPMCALLBACK_TRANS_START: int = 32
RPMCALLBACK_TRANS_STOP: int = 64
RPMCALLBACK_UNINST_PROGRESS: int = 128
RPMCALLBACK_UNINST_START: int = 256
RPMCALLBACK_UNINST_STOP: int = 512
RPMCALLBACK_UNKNOWN: int = 0
RPMCALLBACK_UNPACK_ERROR: int = 8192
RPMCALLBACK_VERIFY_PROGRESS: int = 1048576
RPMCALLBACK_VERIFY_START: int = 2097152
RPMCALLBACK_VERIFY_STOP: int = 4194304
RPMDBI_BASENAMES: int = 1117
RPMDBI_CONFLICTNAME: int = 1054
RPMDBI_DIRNAMES: int = 1118
RPMDBI_GROUP: int = 1016
RPMDBI_INSTALLTID: int = 1128
RPMDBI_INSTFILENAMES: int = 5040
RPMDBI_LABEL: int = 2
RPMDBI_NAME: int = 1000
RPMDBI_OBSOLETENAME: int = 1090
RPMDBI_PACKAGES: int = 0
RPMDBI_PROVIDENAME: int = 1047
RPMDBI_REQUIRENAME: int = 1049
RPMDBI_SHA1HEADER: int = 269
RPMDBI_SIGMD5: int = 261
RPMDBI_TRIGGERNAME: int = 1066
RPMDEP_SENSE_CONFLICTS: int = 1
RPMDEP_SENSE_REQUIRES: int = 0
RPMFILE_ARTIFACT: int = 4096
RPMFILE_CONFIG: int = 1
RPMFILE_DOC: int = 2
RPMFILE_GHOST: int = 64
RPMFILE_ICON: int = 4
RPMFILE_LICENSE: int = 128
RPMFILE_MISSINGOK: int = 8
RPMFILE_NOREPLACE: int = 16
RPMFILE_PUBKEY: int = 2048
RPMFILE_README: int = 256
RPMFILE_SPECFILE: int = 32
RPMFILE_STATE_NETSHARED: int = 3
RPMFILE_STATE_NORMAL: int = 0
RPMFILE_STATE_NOTINSTALLED: int = 2
RPMFILE_STATE_REPLACED: int = 1
RPMFILE_STATE_WRONGCOLOR: int = 4
RPMFI_FLAGS_ERASE: int = 858122
RPMFI_FLAGS_FILETRIGGER: int = 1032190
RPMFI_FLAGS_INSTALL: int = 65538
RPMFI_FLAGS_ONLY_FILENAMES: int = 1048574
RPMFI_FLAGS_QUERY: int = 98318
RPMFI_FLAGS_VERIFY: int = 32782
RPMLOG_ALERT: int = 1
RPMLOG_CRIT: int = 2
RPMLOG_DEBUG: int = 7
RPMLOG_EMERG: int = 0
RPMLOG_ERR: int = 3
RPMLOG_INFO: int = 6
RPMLOG_NOTICE: int = 5
RPMLOG_WARNING: int = 4
RPMMIRE_DEFAULT: int = 0
RPMMIRE_GLOB: int = 3
RPMMIRE_REGEX: int = 2
RPMMIRE_STRCMP: int = 1
RPMPROB_BADARCH: int = 0
RPMPROB_BADOS: int = 1
RPMPROB_BADRELOCATE: int = 3
RPMPROB_CONFLICT: int = 5
RPMPROB_DISKNODES: int = 10
RPMPROB_DISKSPACE: int = 9
RPMPROB_FILE_CONFLICT: int = 7
RPMPROB_FILTER_DISKNODES: int = 256
RPMPROB_FILTER_DISKSPACE: int = 128
RPMPROB_FILTER_FORCERELOCATE: int = 8
RPMPROB_FILTER_IGNOREARCH: int = 2
RPMPROB_FILTER_IGNOREOS: int = 1
RPMPROB_FILTER_OLDPACKAGE: int = 64
RPMPROB_FILTER_REPLACENEWFILES: int = 16
RPMPROB_FILTER_REPLACEOLDFILES: int = 32
RPMPROB_FILTER_REPLACEPKG: int = 4
RPMPROB_FILTER_VERIFY: int = 512
RPMPROB_NEW_FILE_CONFLICT: int = 6
RPMPROB_OBSOLETES: int = 11
RPMPROB_OLDPACKAGE: int = 8
RPMPROB_PKG_INSTALLED: int = 2
RPMPROB_REQUIRES: int = 4
RPMPROB_VERIFY: int = 12
RPMRC_FAIL: int = 2
RPMRC_NOKEY: int = 4
RPMRC_NOTFOUND: int = 1
RPMRC_NOTTRUSTED: int = 3
RPMRC_OK: int = 0
RPMSENSE_ANY: int = 0
RPMSENSE_CONFIG: int = 268435456
RPMSENSE_EQUAL: int = 8
RPMSENSE_FIND_PROVIDES: int = 32768
RPMSENSE_FIND_REQUIRES: int = 16384
RPMSENSE_GREATER: int = 4
RPMSENSE_INTERP: int = 256
RPMSENSE_KEYRING: int = 67108864
RPMSENSE_LESS: int = 2
RPMSENSE_MISSINGOK: int = 524288
RPMSENSE_POSTTRANS: int = 32
RPMSENSE_PREREQ: int = 64
RPMSENSE_PRETRANS: int = 128
RPMSENSE_RPMLIB: int = 16777216
RPMSENSE_SCRIPT_POST: int = 1024
RPMSENSE_SCRIPT_POSTUN: int = 4096
RPMSENSE_SCRIPT_PRE: int = 512
RPMSENSE_SCRIPT_PREUN: int = 2048
RPMSENSE_SCRIPT_VERIFY: int = 8192
RPMSENSE_TRIGGERIN: int = 65536
RPMSENSE_TRIGGERPOSTUN: int = 262144
RPMSENSE_TRIGGERPREIN: int = 33554432
RPMSENSE_TRIGGERUN: int = 131072
RPMSIG_DIGEST_TYPE: int = 1
RPMSIG_NONE_TYPE: int = 0
RPMSIG_SIGNATURE_TYPE: int = 2
RPMSIG_UNVERIFIED_TYPE: int = 1073741824
RPMSIG_VERIFIABLE_TYPE: int = 3
RPMSPEC_ANYARCH: int = 1
RPMSPEC_FORCE: int = 2
RPMSPEC_NOLANG: int = 4
RPMSPEC_NONE: int = 0
RPMTAG_ARCH: int = 1022
RPMTAG_ARCHIVESIZE: int = 1046
RPMTAG_ARCHSUFFIX: int = 5098
RPMTAG_BASENAMES: int = 1117
RPMTAG_BUGURL: int = 5012
RPMTAG_BUILDARCHS: int = 1089
RPMTAG_BUILDHOST: int = 1007
RPMTAG_BUILDTIME: int = 1006
RPMTAG_C: int = 1054
RPMTAG_CHANGELOGNAME: int = 1081
RPMTAG_CHANGELOGTEXT: int = 1082
RPMTAG_CHANGELOGTIME: int = 1080
RPMTAG_CLASSDICT: int = 1142
RPMTAG_CONFLICTFLAGS: int = 1053
RPMTAG_CONFLICTNAME: int = 1054
RPMTAG_CONFLICTNEVRS: int = 5044
RPMTAG_CONFLICTS: int = 1054
RPMTAG_CONFLICTVERSION: int = 1055
RPMTAG_COOKIE: int = 1094
RPMTAG_DBINSTANCE: int = 1195
RPMTAG_DEPENDSDICT: int = 1145
RPMTAG_DESCRIPTION: int = 1005
RPMTAG_DIRINDEXES: int = 1116
RPMTAG_DIRNAMES: int = 1118
RPMTAG_DISTRIBUTION: int = 1010
RPMTAG_DISTTAG: int = 1155
RPMTAG_DISTURL: int = 1123
RPMTAG_DSAHEADER: int = 267
RPMTAG_E: int = 1003
RPMTAG_ENCODING: int = 5062
RPMTAG_ENHANCEFLAGS: int = 5057
RPMTAG_ENHANCENAME: int = 5055
RPMTAG_ENHANCENEVRS: int = 5061
RPMTAG_ENHANCES: int = 5055
RPMTAG_ENHANCEVERSION: int = 5056
RPMTAG_EPOCH: int = 1003
RPMTAG_EPOCHNUM: int = 5019
RPMTAG_EVR: int = 5013
RPMTAG_EXCLUDEARCH: int = 1059
RPMTAG_EXCLUDEOS: int = 1060
RPMTAG_EXCLUSIVEARCH: int = 1061
RPMTAG_EXCLUSIVEOS: int = 1062
RPMTAG_FILECAPS: int = 5010
RPMTAG_FILECLASS: int = 1141
RPMTAG_FILECOLORS: int = 1140
RPMTAG_FILECONTEXTS: int = 1147
RPMTAG_FILEDEPENDSN: int = 1144
RPMTAG_FILEDEPENDSX: int = 1143
RPMTAG_FILEDEVICES: int = 1095
RPMTAG_FILEDIGESTALGO: int = 5011
RPMTAG_FILEDIGESTS: int = 1035
RPMTAG_FILEFLAGS: int = 1037
RPMTAG_FILEGROUPNAME: int = 1040
RPMTAG_FILEINODES: int = 1096
RPMTAG_FILELANGS: int = 1097
RPMTAG_FILELINKTOS: int = 1036
RPMTAG_FILEMD5S: int = 1035
RPMTAG_FILEMODES: int = 1030
RPMTAG_FILEMTIMES: int = 1034
RPMTAG_FILENAMES: int = 5000
RPMTAG_FILENLINKS: int = 5045
RPMTAG_FILEPROVIDE: int = 5001
RPMTAG_FILERDEVS: int = 1033
RPMTAG_FILEREQUIRE: int = 5002
RPMTAG_FILESIGNATURELENGTH: int = 5091
RPMTAG_FILESIGNATURES: int = 5090
RPMTAG_FILESIZES: int = 1028
RPMTAG_FILESTATES: int = 1029
RPMTAG_FILETRIGGERCONDS: int = 5086
RPMTAG_FILETRIGGERFLAGS: int = 5072
RPMTAG_FILETRIGGERINDEX: int = 5070
RPMTAG_FILETRIGGERNAME: int = 5069
RPMTAG_FILETRIGGERPRIORITIES: int = 5084
RPMTAG_FILETRIGGERSCRIPTFLAGS: int = 5068
RPMTAG_FILETRIGGERSCRIPTPROG: int = 5067
RPMTAG_FILETRIGGERSCRIPTS: int = 5066
RPMTAG_FILETRIGGERTYPE: int = 5087
RPMTAG_FILETRIGGERVERSION: int = 5071
RPMTAG_FILEUSERNAME: int = 1039
RPMTAG_FILEVERIFYFLAGS: int = 1045
RPMTAG_FSCONTEXTS: int = 1148
RPMTAG_GIF: int = 1012
RPMTAG_GROUP: int = 1016
RPMTAG_HDRID: int = 269
RPMTAG_HEADERCOLOR: int = 5017
RPMTAG_HEADERI18NTABLE: int = 100
RPMTAG_HEADERIMAGE: int = 61
RPMTAG_HEADERIMMUTABLE: int = 63
RPMTAG_HEADERREGIONS: int = 64
RPMTAG_HEADERSIGNATURES: int = 62
RPMTAG_ICON: int = 1043
RPMTAG_INSTALLCOLOR: int = 1127
RPMTAG_INSTALLTID: int = 1128
RPMTAG_INSTALLTIME: int = 1008
RPMTAG_INSTFILENAMES: int = 5040
RPMTAG_INSTPREFIXES: int = 1099
RPMTAG_LICENSE: int = 1014
RPMTAG_LONGARCHIVESIZE: int = 271
RPMTAG_LONGFILESIZES: int = 5008
RPMTAG_LONGSIGSIZE: int = 270
RPMTAG_LONGSIZE: int = 5009
RPMTAG_MODULARITYLABEL: int = 5096
RPMTAG_N: int = 1000
RPMTAG_NAME: int = 1000
RPMTAG_NEVR: int = 5015
RPMTAG_NEVRA: int = 5016
RPMTAG_NOPATCH: int = 1052
RPMTAG_NOSOURCE: int = 1051
RPMTAG_NOT_FOUND: int = -1
RPMTAG_NVR: int = 5014
RPMTAG_NVRA: int = 1196
RPMTAG_O: int = 1090
RPMTAG_OBSOLETEFLAGS: int = 1114
RPMTAG_OBSOLETENAME: int = 1090
RPMTAG_OBSOLETENEVRS: int = 5043
RPMTAG_OBSOLETES: int = 1090
RPMTAG_OBSOLETEVERSION: int = 1115
RPMTAG_OLDENHANCES: int = 1159
RPMTAG_OLDENHANCESFLAGS: int = 1161
RPMTAG_OLDENHANCESNAME: int = 1159
RPMTAG_OLDENHANCESVERSION: int = 1160
RPMTAG_OLDFILENAMES: int = 1027
RPMTAG_OLDSUGGESTS: int = 1156
RPMTAG_OLDSUGGESTSFLAGS: int = 1158
RPMTAG_OLDSUGGESTSNAME: int = 1156
RPMTAG_OLDSUGGESTSVERSION: int = 1157
RPMTAG_OPTFLAGS: int = 1122
RPMTAG_ORDERFLAGS: int = 5037
RPMTAG_ORDERNAME: int = 5035
RPMTAG_ORDERVERSION: int = 5036
RPMTAG_ORIGBASENAMES: int = 1120
RPMTAG_ORIGDIRINDEXES: int = 1119
RPMTAG_ORIGDIRNAMES: int = 1121
RPMTAG_ORIGFILENAMES: int = 5007
RPMTAG_OS: int = 1021
RPMTAG_P: int = 1047
RPMTAG_PACKAGER: int = 1015
RPMTAG_PATCH: int = 1019
RPMTAG_PATCHESFLAGS: int = 1134
RPMTAG_PATCHESNAME: int = 1133
RPMTAG_PATCHESVERSION: int = 1135
RPMTAG_PAYLOADCOMPRESSOR: int = 1125
RPMTAG_PAYLOADDIGEST: int = 5092
RPMTAG_PAYLOADDIGESTALGO: int = 5093
RPMTAG_PAYLOADDIGESTALT: int = 5097
RPMTAG_PAYLOADFLAGS: int = 1126
RPMTAG_PAYLOADFORMAT: int = 1124
RPMTAG_PKGID: int = 261
RPMTAG_PLATFORM: int = 1132
RPMTAG_POLICIES: int = 1150
RPMTAG_POLICYFLAGS: int = 5033
RPMTAG_POLICYNAMES: int = 5030
RPMTAG_POLICYTYPES: int = 5031
RPMTAG_POLICYTYPESINDEXES: int = 5032
RPMTAG_POSTIN: int = 1024
RPMTAG_POSTINFLAGS: int = 5021
RPMTAG_POSTINPROG: int = 1086
RPMTAG_POSTTRANS: int = 1152
RPMTAG_POSTTRANSFLAGS: int = 5025
RPMTAG_POSTTRANSPROG: int = 1154
RPMTAG_POSTUN: int = 1026
RPMTAG_POSTUNFLAGS: int = 5023
RPMTAG_POSTUNPROG: int = 1088
RPMTAG_PREFIXES: int = 1098
RPMTAG_PREIN: int = 1023
RPMTAG_PREINFLAGS: int = 5020
RPMTAG_PREINPROG: int = 1085
RPMTAG_PRETRANS: int = 1151
RPMTAG_PRETRANSFLAGS: int = 5024
RPMTAG_PRETRANSPROG: int = 1153
RPMTAG_PREUN: int = 1025
RPMTAG_PREUNFLAGS: int = 5022
RPMTAG_PREUNPROG: int = 1087
RPMTAG_PROVIDEFLAGS: int = 1112
RPMTAG_PROVIDENAME: int = 1047
RPMTAG_PROVIDENEVRS: int = 5042
RPMTAG_PROVIDES: int = 1047
RPMTAG_PROVIDEVERSION: int = 1113
RPMTAG_PUBKEYS: int = 266
RPMTAG_R: int = 1002
RPMTAG_RECOMMENDFLAGS: int = 5048
RPMTAG_RECOMMENDNAME: int = 5046
RPMTAG_RECOMMENDNEVRS: int = 5058
RPMTAG_RECOMMENDS: int = 5046
RPMTAG_RECOMMENDVERSION: int = 5047
RPMTAG_RECONTEXTS: int = 1149
RPMTAG_RELEASE: int = 1002
RPMTAG_REMOVETID: int = 1129
RPMTAG_REQUIREFLAGS: int = 1048
RPMTAG_REQUIRENAME: int = 1049
RPMTAG_REQUIRENEVRS: int = 5041
RPMTAG_REQUIRES: int = 1049
RPMTAG_REQUIREVERSION: int = 1050
RPMTAG_RPMVERSION: int = 1064
RPMTAG_RSAHEADER: int = 268
RPMTAG_SHA1HEADER: int = 269
RPMTAG_SHA256HEADER: int = 273
RPMTAG_SIGGPG: int = 262
RPMTAG_SIGMD5: int = 261
RPMTAG_SIGPGP: int = 259
RPMTAG_SIGSIZE: int = 257
RPMTAG_SIZE: int = 1009
RPMTAG_SOURCE: int = 1018
RPMTAG_SOURCEPACKAGE: int = 1106
RPMTAG_SOURCEPKGID: int = 1146
RPMTAG_SOURCERPM: int = 1044
RPMTAG_SPEC: int = 5099
RPMTAG_SUGGESTFLAGS: int = 5051
RPMTAG_SUGGESTNAME: int = 5049
RPMTAG_SUGGESTNEVRS: int = 5059
RPMTAG_SUGGESTS: int = 5049
RPMTAG_SUGGESTVERSION: int = 5050
RPMTAG_SUMMARY: int = 1004
RPMTAG_SUPPLEMENTFLAGS: int = 5054
RPMTAG_SUPPLEMENTNAME: int = 5052
RPMTAG_SUPPLEMENTNEVRS: int = 5060
RPMTAG_SUPPLEMENTS: int = 5052
RPMTAG_SUPPLEMENTVERSION: int = 5053
RPMTAG_TRANSFILETRIGGERCONDS: int = 5088
RPMTAG_TRANSFILETRIGGERFLAGS: int = 5082
RPMTAG_TRANSFILETRIGGERINDEX: int = 5080
RPMTAG_TRANSFILETRIGGERNAME: int = 5079
RPMTAG_TRANSFILETRIGGERPRIORITIES: int = 5085
RPMTAG_TRANSFILETRIGGERSCRIPTFLAGS: int = 5078
RPMTAG_TRANSFILETRIGGERSCRIPTPROG: int = 5077
RPMTAG_TRANSFILETRIGGERSCRIPTS: int = 5076
RPMTAG_TRANSFILETRIGGERTYPE: int = 5089
RPMTAG_TRANSFILETRIGGERVERSION: int = 5081
RPMTAG_TRANSLATIONURL: int = 5100
RPMTAG_TRIGGERCONDS: int = 5005
RPMTAG_TRIGGERFLAGS: int = 1068
RPMTAG_TRIGGERINDEX: int = 1069
RPMTAG_TRIGGERNAME: int = 1066
RPMTAG_TRIGGERSCRIPTFLAGS: int = 5027
RPMTAG_TRIGGERSCRIPTPROG: int = 1092
RPMTAG_TRIGGERSCRIPTS: int = 1065
RPMTAG_TRIGGERTYPE: int = 5006
RPMTAG_TRIGGERVERSION: int = 1067
RPMTAG_UPSTREAMRELEASES: int = 5101
RPMTAG_URL: int = 1020
RPMTAG_V: int = 1001
RPMTAG_VCS: int = 5034
RPMTAG_VENDOR: int = 1011
RPMTAG_VERBOSE: int = 5018
RPMTAG_VERIFYSCRIPT: int = 1079
RPMTAG_VERIFYSCRIPTFLAGS: int = 5026
RPMTAG_VERIFYSCRIPTPROG: int = 1091
RPMTAG_VERITYSIGNATUREALGO: int = 277
RPMTAG_VERITYSIGNATURES: int = 276
RPMTAG_VERSION: int = 1001
RPMTAG_XPM: int = 1013
RPMTRANS_FLAG_ADDINDEPS: int = 0
RPMTRANS_FLAG_ALLFILES: int = 64
RPMTRANS_FLAG_BUILD_PROBS: int = 2
RPMTRANS_FLAG_DEPLOOPS: int = -2147483648
RPMTRANS_FLAG_JUSTDB: int = 8
RPMTRANS_FLAG_KEEPOBSOLETE: int = 0
RPMTRANS_FLAG_NOARTIFACTS: int = 536870912
RPMTRANS_FLAG_NOCAPS: int = 512
RPMTRANS_FLAG_NOCONFIGS: int = 1073741824
RPMTRANS_FLAG_NOCONTEXTS: int = 256
RPMTRANS_FLAG_NODB: int = 1024
RPMTRANS_FLAG_NODOCS: int = 32
RPMTRANS_FLAG_NOFILEDIGEST: int = 134217728
RPMTRANS_FLAG_NOMD5: int = 134217728
RPMTRANS_FLAG_NOPLUGINS: int = 128
RPMTRANS_FLAG_NOPOST: int = 262144
RPMTRANS_FLAG_NOPOSTTRANS: int = 33554432
RPMTRANS_FLAG_NOPOSTUN: int = 4194304
RPMTRANS_FLAG_NOPRE: int = 131072
RPMTRANS_FLAG_NOPRETRANS: int = 16777216
RPMTRANS_FLAG_NOPREUN: int = 2097152
RPMTRANS_FLAG_NOSCRIPTS: int = 4
RPMTRANS_FLAG_NOSUGGEST: int = 0
RPMTRANS_FLAG_NOTRIGGERIN: int = 524288
RPMTRANS_FLAG_NOTRIGGERPOSTUN: int = 8388608
RPMTRANS_FLAG_NOTRIGGERPREIN: int = 65536
RPMTRANS_FLAG_NOTRIGGERS: int = 16
RPMTRANS_FLAG_NOTRIGGERUN: int = 1048576
RPMTRANS_FLAG_REPACKAGE: int = 0
RPMTRANS_FLAG_REVERSE: int = 0
RPMTRANS_FLAG_TEST: int = 1
RPMVERIFY_CAPS: int = 256
RPMVERIFY_FILEDIGEST: int = 1
RPMVERIFY_FILESIZE: int = 2
RPMVERIFY_GROUP: int = 16
RPMVERIFY_LINKTO: int = 4
RPMVERIFY_LSTATFAIL: int = 1073741824
RPMVERIFY_MODE: int = 64
RPMVERIFY_MTIME: int = 32
RPMVERIFY_NONE: int = 0
RPMVERIFY_RDEV: int = 128
RPMVERIFY_READFAIL: int = 536870912
RPMVERIFY_READLINKFAIL: int = 268435456
RPMVERIFY_USER: int = 8
RPMVSF_DEFAULT: int = 0
RPMVSF_MASK_NODIGESTS: int = 197376
RPMVSF_MASK_NOHEADER: int = 3840
RPMVSF_MASK_NOPAYLOAD: int = 983040
RPMVSF_MASK_NOSIGNATURES: int = 789504
RPMVSF_NEEDPAYLOAD: int = 2
RPMVSF_NODSA: int = 262144
RPMVSF_NODSAHEADER: int = 1024
RPMVSF_NOHDRCHK: int = 1
RPMVSF_NOMD5: int = 131072
RPMVSF_NOPAYLOAD: int = 65536
RPMVSF_NORSA: int = 524288
RPMVSF_NORSAHEADER: int = 2048
RPMVSF_NOSHA1HEADER: int = 256
RPMVSF_NOSHA256HEADER: int = 512
TR_ADDED: int = 1
TR_REMOVED: int = 2
TR_RPMDB: int = 4
_RPMVSF_NODIGESTS: int = 197376
_RPMVSF_NOHEADER: int = 3840
_RPMVSF_NOPAYLOAD: int = 983040
_RPMVSF_NOSIGNATURES: int = 789504


header_magic: b'\x8e\xad\xe8\x01\x00\x00\x00\x00'


tagnames: Dict[int, str] = {
  61: 'HEADERIMAGE',
  62: 'HEADERSIGNATURES',
  63: 'HEADERIMMUTABLE',
  64: 'HEADERREGIONS',
  100: 'HEADERI18NTABLE',
  257: 'SIGSIZE',
  259: 'SIGPGP',
  261: 'SIGMD5',
  262: 'SIGGPG',
  266: 'PUBKEYS',
  267: 'DSAHEADER',
  268: 'RSAHEADER',
  269: 'SHA1HEADER',
  270: 'LONGSIGSIZE',
  271: 'LONGARCHIVESIZE',
  273: 'SHA256HEADER',
  276: 'VERITYSIGNATURES',
  277: 'VERITYSIGNATUREALGO',
  1000: 'NAME',
  1001: 'VERSION',
  1002: 'RELEASE',
  1003: 'EPOCH',
  1004: 'SUMMARY',
  1005: 'DESCRIPTION',
  1006: 'BUILDTIME',
  1007: 'BUILDHOST',
  1008: 'INSTALLTIME',
  1009: 'SIZE',
  1010: 'DISTRIBUTION',
  1011: 'VENDOR',
  1012: 'GIF',
  1013: 'XPM',
  1014: 'LICENSE',
  1015: 'PACKAGER',
  1016: 'GROUP',
  1018: 'SOURCE',
  1019: 'PATCH',
  1020: 'URL',
  1021: 'OS',
  1022: 'ARCH',
  1023: 'PREIN',
  1024: 'POSTIN',
  1025: 'PREUN',
  1026: 'POSTUN',
  1027: 'OLDFILENAMES',
  1028: 'FILESIZES',
  1029: 'FILESTATES',
  1030: 'FILEMODES',
  1033: 'FILERDEVS',
  1034: 'FILEMTIMES',
  1035: 'FILEMD5S',
  1036: 'FILELINKTOS',
  1037: 'FILEFLAGS',
  1039: 'FILEUSERNAME',
  1040: 'FILEGROUPNAME',
  1043: 'ICON',
  1044: 'SOURCERPM',
  1045: 'FILEVERIFYFLAGS',
  1046: 'ARCHIVESIZE',
  1047: 'PROVIDES',
  1048: 'REQUIREFLAGS',
  1049: 'REQUIRES',
  1050: 'REQUIREVERSION',
  1051: 'NOSOURCE',
  1052: 'NOPATCH',
  1053: 'CONFLICTFLAGS',
  1054: 'CONFLICTS',
  1055: 'CONFLICTVERSION',
  1059: 'EXCLUDEARCH',
  1060: 'EXCLUDEOS',
  1061: 'EXCLUSIVEARCH',
  1062: 'EXCLUSIVEOS',
  1064: 'RPMVERSION',
  1065: 'TRIGGERSCRIPTS',
  1066: 'TRIGGERNAME',
  1067: 'TRIGGERVERSION',
  1068: 'TRIGGERFLAGS',
  1069: 'TRIGGERINDEX',
  1079: 'VERIFYSCRIPT',
  1080: 'CHANGELOGTIME',
  1081: 'CHANGELOGNAME',
  1082: 'CHANGELOGTEXT',
  1085: 'PREINPROG',
  1086: 'POSTINPROG',
  1087: 'PREUNPROG',
  1088: 'POSTUNPROG',
  1089: 'BUILDARCHS',
  1090: 'OBSOLETES',
  1091: 'VERIFYSCRIPTPROG',
  1092: 'TRIGGERSCRIPTPROG',
  1094: 'COOKIE',
  1095: 'FILEDEVICES',
  1096: 'FILEINODES',
  1097: 'FILELANGS',
  1098: 'PREFIXES',
  1099: 'INSTPREFIXES',
  1106: 'SOURCEPACKAGE',
  1112: 'PROVIDEFLAGS',
  1113: 'PROVIDEVERSION',
  1114: 'OBSOLETEFLAGS',
  1115: 'OBSOLETEVERSION',
  1116: 'DIRINDEXES',
  1117: 'BASENAMES',
  1118: 'DIRNAMES',
  1119: 'ORIGDIRINDEXES',
  1120: 'ORIGBASENAMES',
  1121: 'ORIGDIRNAMES',
  1122: 'OPTFLAGS',
  1123: 'DISTURL',
  1124: 'PAYLOADFORMAT',
  1125: 'PAYLOADCOMPRESSOR',
  1126: 'PAYLOADFLAGS',
  1127: 'INSTALLCOLOR',
  1128: 'INSTALLTID',
  1129: 'REMOVETID',
  1132: 'PLATFORM',
  1133: 'PATCHESNAME',
  1134: 'PATCHESFLAGS',
  1135: 'PATCHESVERSION',
  1140: 'FILECOLORS',
  1141: 'FILECLASS',
  1142: 'CLASSDICT',
  1143: 'FILEDEPENDSX',
  1144: 'FILEDEPENDSN',
  1145: 'DEPENDSDICT',
  1146: 'SOURCEPKGID',
  1147: 'FILECONTEXTS',
  1148: 'FSCONTEXTS',
  1149: 'RECONTEXTS',
  1150: 'POLICIES',
  1151: 'PRETRANS',
  1152: 'POSTTRANS',
  1153: 'PRETRANSPROG',
  1154: 'POSTTRANSPROG',
  1155: 'DISTTAG',
  1156: 'OLDSUGGESTSNAME',
  1157: 'OLDSUGGESTSVERSION',
  1158: 'OLDSUGGESTSFLAGS',
  1159: 'OLDENHANCESNAME',
  1160: 'OLDENHANCESVERSION',
  1161: 'OLDENHANCESFLAGS',
  1195: 'DBINSTANCE',
  1196: 'NVRA',
  5000: 'FILENAMES',
  5001: 'FILEPROVIDE',
  5002: 'FILEREQUIRE',
  5005: 'TRIGGERCONDS',
  5006: 'TRIGGERTYPE',
  5007: 'ORIGFILENAMES',
  5008: 'LONGFILESIZES',
  5009: 'LONGSIZE',
  5010: 'FILECAPS',
  5011: 'FILEDIGESTALGO',
  5012: 'BUGURL',
  5013: 'EVR',
  5014: 'NVR',
  5015: 'NEVR',
  5016: 'NEVRA',
  5017: 'HEADERCOLOR',
  5018: 'VERBOSE',
  5019: 'EPOCHNUM',
  5020: 'PREINFLAGS',
  5021: 'POSTINFLAGS',
  5022: 'PREUNFLAGS',
  5023: 'POSTUNFLAGS',
  5024: 'PRETRANSFLAGS',
  5025: 'POSTTRANSFLAGS',
  5026: 'VERIFYSCRIPTFLAGS',
  5027: 'TRIGGERSCRIPTFLAGS',
  5030: 'POLICYNAMES',
  5031: 'POLICYTYPES',
  5032: 'POLICYTYPESINDEXES',
  5033: 'POLICYFLAGS',
  5034: 'VCS',
  5035: 'ORDERNAME',
  5036: 'ORDERVERSION',
  5037: 'ORDERFLAGS',
  5040: 'INSTFILENAMES',
  5041: 'REQUIRENEVRS',
  5042: 'PROVIDENEVRS',
  5043: 'OBSOLETENEVRS',
  5044: 'CONFLICTNEVRS',
  5045: 'FILENLINKS',
  5046: 'RECOMMENDS',
  5047: 'RECOMMENDVERSION',
  5048: 'RECOMMENDFLAGS',
  5049: 'SUGGESTS',
  5050: 'SUGGESTVERSION',
  5051: 'SUGGESTFLAGS',
  5052: 'SUPPLEMENTS',
  5053: 'SUPPLEMENTVERSION',
  5054: 'SUPPLEMENTFLAGS',
  5055: 'ENHANCES',
  5056: 'ENHANCEVERSION',
  5057: 'ENHANCEFLAGS',
  5058: 'RECOMMENDNEVRS',
  5059: 'SUGGESTNEVRS',
  5060: 'SUPPLEMENTNEVRS',
  5061: 'ENHANCENEVRS',
  5062: 'ENCODING',
  5066: 'FILETRIGGERSCRIPTS',
  5067: 'FILETRIGGERSCRIPTPROG',
  5068: 'FILETRIGGERSCRIPTFLAGS',
  5069: 'FILETRIGGERNAME',
  5070: 'FILETRIGGERINDEX',
  5071: 'FILETRIGGERVERSION',
  5072: 'FILETRIGGERFLAGS',
  5076: 'TRANSFILETRIGGERSCRIPTS',
  5077: 'TRANSFILETRIGGERSCRIPTPROG',
  5078: 'TRANSFILETRIGGERSCRIPTFLAGS',
  5079: 'TRANSFILETRIGGERNAME',
  5080: 'TRANSFILETRIGGERINDEX',
  5081: 'TRANSFILETRIGGERVERSION',
  5082: 'TRANSFILETRIGGERFLAGS',
  5084: 'FILETRIGGERPRIORITIES',
  5085: 'TRANSFILETRIGGERPRIORITIES',
  5086: 'FILETRIGGERCONDS',
  5087: 'FILETRIGGERTYPE',
  5088: 'TRANSFILETRIGGERCONDS',
  5089: 'TRANSFILETRIGGERTYPE',
  5090: 'FILESIGNATURES',
  5091: 'FILESIGNATURELENGTH',
  5092: 'PAYLOADDIGEST',
  5093: 'PAYLOADDIGESTALGO',
  5096: 'MODULARITYLABEL',
  5097: 'PAYLOADDIGESTALT',
  5098: 'ARCHSUFFIX',
  5099: 'SPEC',
  5100: 'TRANSLATIONURL',
  5101: 'UPSTREAMRELEASES',
}


class archive:
    def close(self) -> Any: ...
    def hascontent(self) -> Any: ...
    def read(self, size = ...) -> Any: ...
    def readto(self, fd, nodigest = ...) -> Any: ...
    def tell(self) -> Any: ...
    def write(self, buffer) -> Any: ...
    def writeto(self, fd) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...


class ds:
    def __init__(self, *args, **kwargs):
        pass

    def Color(self, *args, **kwargs) -> Any: ...
    def Compare(self, *args, **kwargs) -> Any: ...
    def Count(self, *args, **kwargs) -> Any: ...
    def DNEVR(self, *args, **kwargs) -> Any: ...
    def EVR(self, *args, **kwargs) -> Any: ...
    def Find(self, *args, **kwargs) -> Any: ...
    def Flags(self, *args, **kwargs) -> Any: ...
    def Instance(self) -> Any: ...
    def IsReverse(self) -> Any: ...
    def IsRich(self) -> Any: ...
    def IsWeak(self) -> Any: ...
    def Ix(self, *args, **kwargs) -> Any: ...
    def Merge(self, *args, **kwargs) -> Any: ...
    def N(self, *args, **kwargs) -> Any: ...
    def Rpmlib(self, *args, **kwargs) -> Any: ...
    def Search(self, *args, **kwargs) -> Any: ...
    def SetNoPromote(self, noPromote) -> Any: ...
    def Sort(self, *args, **kwargs) -> Any: ...
    def TagN(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> Any: ...
    def __next__(self) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...


class error(Exception):
    pass


class fd:
    closed: Any
    flags: Any
    mode: Any
    name: Any

    def __init__(self, *args, **kwargs):
        pass

    def close(self, *args, **kwargs) -> Any: ...
    def fileno(self, *args, **kwargs) -> Any: ...
    def flush(self, *args, **kwargs) -> Any: ...
    def isatty(self, *args, **kwargs) -> Any: ...
    @classmethod
    def open(cls, *args, **kwargs) -> Any: ...
    def read(self, *args, **kwargs) -> Any: ...
    def seek(self, *args, **kwargs) -> Any: ...
    def tell(self, *args, **kwargs) -> Any: ...
    def write(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...


class fi:
    def __init__(self, *args, **kwargs):
        pass

    def BN(self) -> Any: ...
    def DC(self) -> Any: ...
    def DN(self) -> Any: ...
    def DX(self) -> Any: ...
    def Digest(self, *args, **kwargs) -> Any: ...
    def FC(self) -> Any: ...
    def FClass(self, *args, **kwargs) -> Any: ...
    def FColor(self, *args, **kwargs) -> Any: ...
    def FFlags(self) -> Any: ...
    def FGroup(self, *args, **kwargs) -> Any: ...
    def FLink(self, *args, **kwargs) -> Any: ...
    def FLinks(self, *args, **kwargs) -> Any: ...
    def FMode(self) -> Any: ...
    def FMtime(self, *args, **kwargs) -> Any: ...
    def FN(self) -> Any: ...
    def FRdev(self, *args, **kwargs) -> Any: ...
    def FSize(self, *args, **kwargs) -> Any: ...
    def FState(self) -> Any: ...
    def FUser(self, *args, **kwargs) -> Any: ...
    def FX(self) -> Any: ...
    def FindFN(self, pathname) -> Any: ...
    def MD5(self, *args, **kwargs) -> Any: ...
    def VFlags(self) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> Any: ...
    def __next__(self) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...


class file:
    basename: Any
    caps: Any
    # class: Any
    color: Any
    digest: Any
    dirname: Any
    dx: Any
    fflags: Any
    fx: Any
    group: Any
    imasig: Any
    inode: Any
    langs: Any
    links: Any
    linkto: Any
    mode: Any
    mtime: Any
    name: Any
    nlink: Any
    orig_basename: Any
    orig_dirname: Any
    orig_name: Any
    rdev: Any
    size: Any
    state: Any
    user: Any
    veritysig: Any
    vflags: Any

    def matches(self, *args, **kwargs) -> Any: ...
    def verify(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...


class files:

    def __init__(self, *args, **kwargs):
        pass

    def archive(self, fd, write = ...) -> Any: ...
    def find(self, filename, orig = ...) -> Any: ...
    def __contains__(self, other) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __len__(self) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...


class hdr:

    def __init__(self, *args, **kwargs):
        pass

    def compressFilelist(self, *args, **kwargs) -> Any: ...
    def convert(self, op = ...) -> Any: ...
    def dsFromHeader(self, to = ..., flags = ...) -> Any: ...
    def dsOfHeader(self) -> Any: ...
    def expandFilelist(self, *args, **kwargs) -> Any: ...
    def fiFromHeader(self) -> Any: ...
    def format(self, format) -> Any: ...
    def fullFilelist(self, *args, **kwargs) -> Any: ...
    def isSource(self) -> Any: ...
    def keys(self) -> Any: ...
    def sprintf(self, *args, **kwargs) -> Any: ...
    def unload(self) -> Any: ...
    def write(self, file, magic = ...) -> Any: ...
    def __contains__(self, other) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __delitem__(self, other) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __hash__(self) -> Any: ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...
    def __setitem__(self, index, object) -> Any: ...


class ii:
    def instances(self, *args, **kwargs) -> Any: ...
    def __bool__(self) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...


class keyring:

    def __init__(self, *args, **kwargs):
        pass

    def addKey(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...


class mi:
    def count(self, *args, **kwargs) -> Any: ...
    def instance(self) -> Any: ...
    def pattern(self, TagN, mire_type, pattern) -> Any: ...
    def __bool__(self) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> Any: ...
    def __next__(self) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...


class prob:
    _num: Any
    _str: Any
    altNEVR: Any
    key: Any
    pkgNEVR: Any
    type: Any

    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...


class pubkey:

    def __init__(self, *args, **kwargs):
        pass

    def base64(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...


class spec:
    build: Any
    check: Any
    clean: Any
    install: Any
    packages: Any
    parsed: Any
    prep: Any
    sourceHeader: Any
    sources: Any

    def __init__(self, *args, **kwargs):
        pass


class specPkg:
    fileFile: Any
    fileList: Any
    header: Any
    policyList: Any

    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...


class strpool:

    def __init__(self, *args, **kwargs):
        pass

    def freeze(self, *args, **kwargs) -> Any: ...
    def id2str(self, *args, **kwargs) -> Any: ...
    def str2id(self, *args, **kwargs) -> Any: ...
    def unfreeze(self, *args, **kwargs) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __len__(self) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...


class te:
    def A(self) -> Any: ...
    def Color(self) -> Any: ...
    def DBOffset(self) -> Any: ...
    def DS(self, TagN) -> Any: ...
    def E(self) -> Any: ...
    def FI(self, TagN) -> Any: ...
    def Failed(self) -> Any: ...
    def Files(self) -> Any: ...
    def Key(self) -> Any: ...
    def N(self) -> Any: ...
    def NEVR(self) -> Any: ...
    def NEVRA(self) -> Any: ...
    def O(self) -> Any: ...
    def Parent(self) -> Any: ...
    def PkgFileSize(self) -> Any: ...
    def Problems(self) -> Any: ...
    def R(self) -> Any: ...
    def SetUserdata(self) -> Any: ...
    def Type(self) -> Any: ...
    def Userdata(self) -> Any: ...
    def V(self) -> Any: ...
    def Verified(self) -> Any: ...
    def __delattr__(self, name) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...


class ts:
    _color: Any
    _flags: Any
    _prefcolor: Any
    _vfyflags: Any
    _vfylevel: Any
    _vsflags: Any
    cbStyle: Any
    rootDir: Any
    scriptFd: Any
    tid: Any

    def __init__(self, *args, **kwargs):
        pass

    def addErase(self, name) -> Any: ...
    def addInstall(self, hdr, data, mode) -> Any: ...
    def addReinstall(self, hdr, data) -> Any: ...
    def addRestore(self, hdr) -> Any: ...
    def check(self, *args, **kwargs) -> Any: ...
    def clean(self) -> Any: ...
    def clear(self) -> None: ...
    def closeDB(self) -> None: ...
    def dbCookie(self, *args, **kwargs) -> Any: ...
    def dbIndex(self, TagN) -> ii: ...
    def dbMatch(self, *args, **kwargs) -> Any: ...
    def getKeyring(self, autoload = ...) -> Any: ...
    def hdrCheck(self, hdrblob) -> Any: ...
    def hdrFromFdno(self, fdno) -> hdr: ...
    def initDB(self) -> None: ...
    def openDB(self) -> Any: ...
    def order(self) -> Any: ...
    def pgpImportPubkey(self, pubkey) -> Any: ...
    def pgpPrtPkts(self, octets) -> Any: ...
    def problems(self) -> Any: ...
    def rebuildDB(self) -> None: ...
    def run(self, *args, **kwargs) -> Any: ...
    def setKeyring(self, keyring) -> Any: ...
    def verifyDB(self) -> None: ...
    def __delattr__(self, name) -> Any: ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...


class ver:
    e: str
    evr: str
    r: str
    v: str

    def __init__(self, evr: str):
        pass


def addMacro(*args, **kwargs) -> Any: ...
def addSign(*args, **kwargs) -> Any: ...
def archscore(archname) -> Any: ...
def blockSignals(*args, **kwargs) -> Any: ...
def checkSignals() -> Any: ...
def delMacro(*args, **kwargs) -> Any: ...
def delSign(*args, **kwargs) -> Any: ...
def expandMacro(string, numeric = ...) -> Any: ...
def labelCompare(version0, version1) -> Any: ...
def log(level, msg) -> Any: ...
def mergeHeaderListFromFD(*args, **kwargs) -> Any: ...
def reloadConfig(target = ...) -> Any: ...
def setInterruptSafety(on = ...) -> Any: ...
def setLogFile(file) -> Any: ...
def setStats(bool) -> Any: ...
def setVerbosity(level) -> Any: ...
def signalCaught(signo) -> Any: ...
def versionCompare(version0, version1) -> Any: ...


# The end.

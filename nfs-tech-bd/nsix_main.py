# bal
import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))

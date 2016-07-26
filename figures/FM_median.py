import cPickle, base64
try:
	from SimpleSession.versions.v64 import beginRestore,\
	    registerAfterModelsCB, reportRestoreError, checkVersion
except ImportError:
	from chimera import UserError
	raise UserError('Cannot open session that was saved in a'
	    ' newer version of Chimera; update your version')
checkVersion([1, 11, 41179])
import chimera
from chimera import replyobj
replyobj.status('Restoring session...', \
    blankAfter=0)
replyobj.status('Beginning session restore...', \
    blankAfter=0, secondary=True)
beginRestore()

def restoreCoreModels():
	from SimpleSession.versions.v64 import init, restoreViewer, \
	     restoreMolecules, restoreColors, restoreSurfaces, \
	     restoreVRML, restorePseudoBondGroups, restoreModelAssociations
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwFOfYdVCWJhbGxTY2FsZXEDSwFHP9AAAAAAAAB9h1UJcG9pbnRTaXplcQRLAUc/8AAAAAAAAH2HVQVjb2xvcnEFSwFLAH2HVQpyaWJib25UeXBlcQZLAUsAfYdVCnN0aWNrU2NhbGVxB0sBRz/wAAAAAAAAfYdVDGFyb21hdGljTW9kZXEISwFLAX2HVQp2ZHdEZW5zaXR5cQlLAUdAFAAAAAAAAH2HVQZoaWRkZW5xCksBiX2HVQ1hcm9tYXRpY0NvbG9ycQtLAU59h1UPcmliYm9uU21vb3RoaW5ncQxLAUsAfYdVCWF1dG9jaGFpbnENSwGIfYdVCnBkYlZlcnNpb25xDksBSwJ9h1UIb3B0aW9uYWxxD31xEFUIb3BlbmVkQXNxEYiJSwEoWEgAAAAvVXNlcnMvY2FybG9zZ29uemFsZXpvbGl2ZXIvTWFzdGVycy9Wb2dlbC1NRC1BbmFseXNpcy9EYXRhL0ZNX21lZGlhbi5wZGJxElUDUERCcRNOiXRxFH2Hh3NVD2xvd2VyQ2FzZUNoYWluc3EVSwGJfYdVCWxpbmVXaWR0aHEWSwFHP/AAAAAAAAB9h1UPcmVzaWR1ZUxhYmVsUG9zcRdLAUsAfYdVBG5hbWVxGEsBWA0AAABGTV9tZWRpYW4ucGRifYdVD2Fyb21hdGljRGlzcGxheXEZSwGJfYdVD3JpYmJvblN0aWZmbmVzc3EaSwFHP+mZmZmZmZp9h1UKcGRiSGVhZGVyc3EbXXEcfXEdYVUDaWRzcR5LAUsASwCGfYdVDnN1cmZhY2VPcGFjaXR5cR9LAUe/8AAAAAAAAH2HVRBhcm9tYXRpY0xpbmVUeXBlcSBLAUsCfYdVFHJpYmJvbkhpZGVzTWFpbmNoYWlucSFLAYh9h1UHZGlzcGxheXEiSwGIfYd1Lg=='))
	resInfo = cPickle.loads(base64.b64decode('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'))
	atomInfo = cPickle.loads(base64.b64decode('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'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVjb2xvcnECTQ0BTn2HVQVhdG9tc3EDXXEEKF1xBShLKEspZV1xBihLKUssZV1xByhLKUsuZV1xCChLKUsqZV1xCShLKksrZV1xCihLLUsoZV1xCyhLL0swZV1xDChLMEsxZV1xDShLMEszZV1xDihLMEs1ZV1xDyhLMUsyZV1xEChLNEsvZV1xEShLKksvZV1xEihLNks3ZV1xEyhLN0s4ZV1xFChLN0s8ZV1xFShLN0s6ZV1xFihLOEs5ZV1xFyhLO0s2ZV1xGChLMUs2ZV1xGShLPUs+ZV1xGihLPktDZV1xGyhLPks/ZV1xHChLP0tAZV1xHShLQks9ZV1xHihLOEs9ZV1xHyhLREtFZV1xIChLRUtKZV1xIShLRUtIZV1xIihLRUtGZV1xIyhLRktHZV1xJChLSUtEZV1xJShLP0tEZV1xJihLS0tMZV1xJyhLTEtRZV1xKChLTEtPZV1xKShLTEtNZV1xKihLTUtOZV1xKyhLUEtLZV1xLChLRktLZV1xLShLUktTZV1xLihLU0tYZV1xLyhLU0tWZV1xMChLU0tUZV1xMShLVEtVZV1xMihLV0tSZV1xMyhLTUtSZV1xNChLWUtaZV1xNShLWktfZV1xNihLWktdZV1xNyhLWktbZV1xOChLW0tcZV1xOShLXktZZV1xOihLVEtZZV1xOyhLYEthZV1xPChLYUtmZV1xPShLYUtkZV1xPihLYUtiZV1xPyhLYktjZV1xQChLZUtgZV1xQShLW0tgZV1xQihLZ0toZV1xQyhLaEttZV1xRChLaEtrZV1xRShLaEtpZV1xRihLaUtqZV1xRyhLbEtnZV1xSChLYktnZV1xSShLbktvZV1xSihLb0t0ZV1xSyhLb0tyZV1xTChLb0twZV1xTShLcEtxZV1xTihLc0tuZV1xTyhLaUtuZV1xUChLdUt2ZV1xUShLdkt3ZV1xUihLdkt5ZV1xUyhLdkt7ZV1xVChLd0t4ZV1xVShLekt1ZV1xVihLcEt1ZV1xVyhLfEt9ZV1xWChLfUuCZV1xWShLfUuAZV1xWihLfUt+ZV1xWyhLfkt/ZV1xXChLgUt8ZV1xXShLd0t8ZV1xXihLg0uEZV1xXyhLhEuJZV1xYChLhEuHZV1xYShLhEuFZV1xYihLhUuGZV1xYyhLiEuDZV1xZChLfkuDZV1xZShLikuLZV1xZihLi0uQZV1xZyhLi0uOZV1xaChLi0uMZV1xaShLjEuNZV1xaihLj0uKZV1xayhLhUuKZV1xbChLkUuSZV1xbShLkkuTZV1xbihLkkuVZV1xbyhLkkuXZV1xcChLk0uUZV1xcShLlkuRZV1xcihLjEuRZV1xcyhLmEuZZV1xdChLmUueZV1xdShLmUucZV1xdihLmUuaZV1xdyhLmkubZV1xeChLnUuYZV1xeShLk0uYZV1xeihLn0ugZV1xeyhLoEulZV1xfChLoEujZV1xfShLoEuhZV1xfihLoUuiZV1xfyhLpEufZV1xgChLmkufZV1xgShLpkunZV1xgihLp0usZV1xgyhLp0uqZV1xhChLp0uoZV1xhShLqEupZV1xhihLq0umZV1xhyhLoUumZV1xiChLrUuuZV1xiShLrkuzZV1xiihLrkuxZV1xiyhLrkuvZV1xjChLr0uwZV1xjShLskutZV1xjihLqEutZV1xjyhLtEu1ZV1xkChLtUu6ZV1xkShLtUu4ZV1xkihLtUu2ZV1xkyhLtku3ZV1xlChLuUu0ZV1xlShLr0u0ZV1xlihLu0u8ZV1xlyhLvEvBZV1xmChLvEu/ZV1xmShLvEu9ZV1xmihLvUu+ZV1xmyhLwEu7ZV1xnChLtku7ZV1xnShLwkvDZV1xnihLw0vIZV1xnyhLw0vGZV1xoChLw0vEZV1xoShLxEvFZV1xoihLx0vCZV1xoyhLvUvCZV1xpChLyUvKZV1xpShLykvPZV1xpihLykvLZV1xpyhLy0vMZV1xqChLzkvJZV1xqShLxEvJZV1xqihL0EvRZV1xqyhL0UvWZV1xrChL0UvUZV1xrShL0UvSZV1xrihL0kvTZV1xryhL1UvQZV1xsChLy0vQZV1xsShL10vYZV1xsihL2EvZZV1xsyhL2EvbZV1xtChL2EvdZV1xtShL2UvaZV1xtihL3EvXZV1xtyhL0kvXZV1xuChL3kvfZV1xuShL30vkZV1xuihL30viZV1xuyhL30vgZV1xvChL4EvhZV1xvShL40veZV1xvihL2UveZV1xvyhL5UvmZV1xwChL5kvrZV1xwShL5kvpZV1xwihL5kvnZV1xwyhL50voZV1xxChL6kvlZV1xxShL4EvlZV1xxihL7EvtZV1xxyhL7UvyZV1xyChL7UvwZV1xyShL7UvuZV1xyihL7kvvZV1xyyhL8UvsZV1xzChL50vsZV1xzShL80v0ZV1xzihL9Ev1ZV1xzyhL9Ev3ZV1x0ChL9Ev5ZV1x0ShL9Uv2ZV1x0ihL+EvzZV1x0yhL7kvzZV1x1ChL+kv7ZV1x1ShL+00AAWVdcdYoS/tL/mVdcdcoS/tL/GVdcdgoS/xL/WVdcdkoS/9L+mVdcdooS/VL+mVdcdsoTQEBTQIBZV1x3ChNAgFNBwFlXXHdKE0CAU0FAWVdcd4oTQIBTQMBZV1x3yhNAwFNBAFlXXHgKE0GAU0BAWVdceEoS/xNAQFlXXHiKE0IAU0JAWVdceMoTQkBTQ4BZV1x5ChNCQFNDAFlXXHlKE0JAU0KAWVdceYoTQoBTQsBZV1x5yhNDQFNCAFlXXHoKE0DAU0IAWVdcekoTQ8BTRABZV1x6ihNEAFNFQFlXXHrKE0QAU0RAWVdcewoTREBTRIBZV1x7ShNFAFNDwFlXXHuKE0KAU0PAWVdce8oTRYBTRcBZV1x8ChNFwFNHAFlXXHxKE0XAU0aAWVdcfIoTRcBTRgBZV1x8yhNGAFNGQFlXXH0KE0bAU0WAWVdcfUoTREBTRYBZV1x9ihNHQFNHgFlXXH3KE0eAU0jAWVdcfgoTR4BTSEBZV1x+ShNHgFNHwFlXXH6KE0fAU0gAWVdcfsoTSIBTR0BZV1x/ChNGAFNHQFlXXH9KE0kAU0lAWVdcf4oTSUBTSoBZV1x/yhNJQFNKAFlXXIAAQAAKE0lAU0mAWVdcgEBAAAoTSYBTScBZV1yAgEAAChNKQFNJAFlXXIDAQAAKE0fAU0kAWVdcgQBAAAoTSsBTSwBZV1yBQEAAChNLAFNLQFlXXIGAQAAKE0sAU0vAWVdcgcBAAAoTSwBTTEBZV1yCAEAAChNLQFNLgFlXXIJAQAAKE0wAU0rAWVdcgoBAAAoTSYBTSsBZV1yCwEAAChNMgFNMwFlXXIMAQAAKE0zAU04AWVdcg0BAAAoTTMBTTcBZV1yDgEAAChNMwFNNAFlXXIPAQAAKE00AU01AWVdchABAAAoTTYBTTIBZV1yEQEAAChNLQFNMgFlZVUFbGFiZWxyEgEAAE0NAVgAAAAAfYdVCGhhbGZib25kchMBAABNDQGIfYdVBnJhZGl1c3IUAQAATQ0BRz/JmZmgAAAAfYdVC2xhYmVsT2Zmc2V0chUBAABNDQFOfYdVCGRyYXdNb2RlchYBAABNDQFLAX2HVQhvcHRpb25hbHIXAQAAfVUHZGlzcGxheXIYAQAATQ0BSwJ9h3Uu'))
	crdInfo = cPickle.loads(base64.b64decode('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'))
	surfInfo = {'category': (1, u'main', {}), 'probeRadius': (1, 1.4, {}), 'pointSize': (1, 1, {}), 'name': [u'MSMS main surface of FM_median.pdb'], 'density': (1, 2, {}), 'colorMode': (1, 1, {}), 'useLighting': (1, True, {}), 'transparencyBlendMode': (1, 1, {}), 'molecule': [0], 'smoothLines': (1, False, {}), 'lineWidth': (1, 1, {}), 'allComponents': (1, True, {}), 'twoSidedLighting': (1, True, {}), 'customVisibility': [None], 'drawMode': (1, 0, {}), 'display': (1, True, {}), 'customColors': [(0, None, {})]}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {'Ru': ((0.141176, 0.560784, 0.560784), 1, u'default'), 'Re': ((0.14902, 0.490196, 0.670588), 1, u'default'), 'Rf': ((0.8, 0, 0.34902), 1, u'default'), 'Ra': ((0, 0.490196, 0), 1, u'default'), 'Rb': ((0.439216, 0.180392, 0.690196), 1, u'default'), 'Rn': ((0.258824, 0.509804, 0.588235), 1, u'default'), 'Rh': ((0.0392157, 0.490196, 0.54902), 1, u'default'), 'Be': ((0.760784, 1, 0), 1, u'default'), 'Ba': ((0, 0.788235, 0), 1, u'default'), 'Bh': ((0.878431, 0, 0.219608), 1, u'default'), 'Bi': ((0.619608, 0.309804, 0.709804), 1, u'default'), 'Bk': ((0.541176, 0.309804, 0.890196), 1, u'default'), 'Br': ((0.65098, 0.160784, 0.160784), 1, u'default'), 'H': ((1, 1, 1), 1, u'default'), 'P': ((1, 0.501961, 0), 1, u'default'), 'Os': ((0.14902, 0.4, 0.588235), 1, u'default'), 'Ge': ((0.4, 0.560784, 0.560784), 1, u'default'), 'Gd': ((0.270588, 1, 0.780392), 1, u'default'), 'Ga': ((0.760784, 0.560784, 0.560784), 1, u'default'), 'Pr': ((0.85098, 1, 0.780392), 1, u'default'), 'Pt': ((0.815686, 0.815686, 0.878431), 1, u'default'), 'Pu': ((0, 0.419608, 1), 1, u'default'),
'C': ((0.564706, 0.564706, 0.564706), 1, u'default'), 'Pb': ((0.341176, 0.34902, 0.380392), 1, u'default'), 'Pa': ((0, 0.631373, 1), 1, u'default'), 'Pd': ((0, 0.411765, 0.521569), 1, u'default'), 'Cd': ((1, 0.85098, 0.560784), 1, u'default'), 'Po': ((0.670588, 0.360784, 0), 1, u'default'), 'Pm': ((0.639216, 1, 0.780392), 1, u'default'), 'Hs': ((0.901961, 0, 0.180392), 1, u'default'), 'Ho': ((0, 1, 0.611765), 1, u'default'), 'Hf': ((0.301961, 0.760784, 1), 1, u'default'), 'Hg': ((0.721569, 0.721569, 0.815686), 1, u'default'), 'He': ((0.85098, 1, 1), 1, u'default'), 'Md': ((0.701961, 0.0509804, 0.65098), 1, u'default'), 'Mg': ((0.541176, 1, 0), 1, u'default'), 'K': ((0.560784, 0.25098, 0.831373), 1, u'default'), 'Mn': ((0.611765, 0.478431, 0.780392), 1, u'default'), 'O': ((1, 0.0509804, 0.0509804), 1, u'default'), 'Mt': ((0.921569, 0, 0.14902), 1, u'default'), 'S': ((1, 1, 0.188235), 1, u'default'), 'W': ((0.129412, 0.580392, 0.839216), 1, u'default'), 'Zn': ((0.490196, 0.501961, 0.690196), 1, u'default'), 'Eu': ((0.380392, 1, 0.780392), 1, u'default'),
'Zr': ((0.580392, 0.878431, 0.878431), 1, u'default'), 'Er': ((0, 0.901961, 0.458824), 1, u'default'), 'Ni': ((0.313725, 0.815686, 0.313725), 1, u'default'), 'No': ((0.741176, 0.0509804, 0.529412), 1, u'default'), 'Na': ((0.670588, 0.360784, 0.94902), 1, u'default'), 'Nb': ((0.45098, 0.760784, 0.788235), 1, u'default'), 'Nd': ((0.780392, 1, 0.780392), 1, u'default'), 'Ne': ((0.701961, 0.890196, 0.960784), 1, u'default'), 'Np': ((0, 0.501961, 1), 1, u'default'), 'Fr': ((0.258824, 0, 0.4), 1, u'default'), 'Fe': ((0.878431, 0.4, 0.2), 1, u'default'), 'Fm': ((0.701961, 0.121569, 0.729412), 1, u'default'), 'B': ((1, 0.709804, 0.709804), 1, u'default'), 'F': ((0.564706, 0.878431, 0.313725), 1, u'default'), 'Sr': ((0, 1, 0), 1, u'default'), 'N': ((0.188235, 0.313725, 0.972549), 1, u'default'), 'Kr': ((0.360784, 0.721569, 0.819608), 1, u'default'), 'Si': ((0.941176, 0.784314, 0.627451), 1, u'default'), 'Sn': ((0.4, 0.501961, 0.501961), 1, u'default'), 'Sm': ((0.560784, 1, 0.780392), 1, u'default'), 'V': ((0.65098, 0.65098, 0.670588), 1, u'default'), 'Sc': ((0.901961, 0.901961, 0.901961), 1, u'default'),
'Sb': ((0.619608, 0.388235, 0.709804), 1, u'default'), 'Sg': ((0.85098, 0, 0.270588), 1, u'default'), 'Se': ((1, 0.631373, 0), 1, u'default'), 'Co': ((0.941176, 0.564706, 0.627451), 1, u'default'), 'Cm': ((0.470588, 0.360784, 0.890196), 1, u'default'), 'Cl': ((0.121569, 0.941176, 0.121569), 1, u'default'), 'Ca': ((0.239216, 1, 0), 1, u'default'), 'Cf': ((0.631373, 0.211765, 0.831373), 1, u'default'), 'Ce': ((1, 1, 0.780392), 1, u'default'), 'Xe': ((0.258824, 0.619608, 0.690196), 1, u'default'), 'Tm': ((0, 0.831373, 0.321569), 1, u'default'), 'Cs': ((0.341176, 0.0901961, 0.560784), 1, u'default'), 'Cr': ((0.541176, 0.6, 0.780392), 1, u'default'), 'Cu': ((0.784314, 0.501961, 0.2), 1, u'default'), 'La': ((0.439216, 0.831373, 1), 1, u'default'), 'Li': ((0.8, 0.501961, 1), 1, u'default'), 'Tl': ((0.65098, 0.329412, 0.301961), 1, u'default'), 'Lu': ((0, 0.670588, 0.141176), 1, u'default'), 'Lr': ((0.780392, 0, 0.4), 1, u'default'), 'Th': ((0, 0.729412, 1), 1, u'default'), 'Ti': ((0.74902, 0.760784, 0.780392), 1, u'default'), 'tan': ((0.823529, 0.705882, 0.54902), 1, u'default'),
'Te': ((0.831373, 0.478431, 0), 1, u'default'), 'Tb': ((0.188235, 1, 0.780392), 1, u'default'), 'Tc': ((0.231373, 0.619608, 0.619608), 1, u'default'), 'Ta': ((0.301961, 0.65098, 1), 1, u'default'), 'Yb': ((0, 0.74902, 0.219608), 1, u'default'), 'Db': ((0.819608, 0, 0.309804), 1, u'default'), 'Dy': ((0.121569, 1, 0.780392), 1, u'default'), 'At': ((0.458824, 0.309804, 0.270588), 1, u'default'), 'I': ((0.580392, 0, 0.580392), 1, u'default'), 'U': ((0, 0.560784, 1), 1, u'default'), 'Y': ((0.580392, 1, 1), 1, u'default'), 'Ac': ((0.439216, 0.670588, 0.980392), 1, u'default'), 'Ag': ((0.752941, 0.752941, 0.752941), 1, u'default'), 'Ir': ((0.0901961, 0.329412, 0.529412), 1, u'default'), 'Am': ((0.329412, 0.360784, 0.94902), 1, u'default'), 'Al': ((0.74902, 0.65098, 0.65098), 1, u'default'), 'As': ((0.741176, 0.501961, 0.890196), 1, u'default'), 'Ar': ((0.501961, 0.819608, 0.890196), 1, u'default'), 'Au': ((1, 0.819608, 0.137255), 1, u'default'), 'Es': ((0.701961, 0.121569, 0.831373), 1, u'default'), 'In': ((0.65098, 0.458824, 0.45098), 1, u'default'), 'Mo': ((0.329412, 0.709804, 0.709804), 1, u'default')}
	materials = {u'default': ((0.85, 0.85, 0.85), 30)}
	pbInfo = {'category': [u'distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'labelOffset': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 40, {}), 'optional': {'fixedLabels': (True, False, (1, False, {}))}, 'display': (1, True, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = (42, (u'', (0, 0.316126, 1, 1)), {(u'', (0.315726, 1, 0, 1)): [23], (u'', (1, 0.105642, 0, 1)): [38], (u'tan', (0.823529, 0.705882, 0.54902, 1)): [0], (u'', (0, 1, 0.210484, 1)): [18], (u'', (0, 1, 0.105242, 1)): [19], (u'', (1, 0.947579, 0, 1)): [30], (u'', (1, 0.526611, 0, 1)): [34], (u'', (0, 1, 0.631453, 1)): [14], (u'', (0, 1, 0.315726, 1)): [17], (u'', (0.105242, 1, 0, 1)): [21], (u'', (1, 0.737095, 0, 1)): [32], (u'', (0, 0.421368, 1, 1)): [5], (u'', (0, 1, 0.947179, 1)): [11], (u'', (1, 0.316126, 0, 1)): [36], (u'yellow', (1, 1, 0, 1)): [40], (u'', (0, 1, 0.736695, 1)): [13], (u'', (1, 0.0004, 0, 1)): [39], (u'', (0, 0.105642, 1, 1)): [2], (u'', (0, 1, 0.841937, 1)): [12], (u'', (0.210484, 1, 0, 1)): [22], (u'', (0, 0.947579, 1, 1)): [10], (u'', (1, 0.631853, 0, 1)): [33], (u'', (0, 0.631853, 1, 1)): [7], (u'', (0.631453, 1, 0, 1)): [26], (u'', (0, 0.210884, 1, 1)): [3], (u'', (1, 0.842337, 0, 1)): [31], (u'', (0, 0.842337, 1, 1)): [9], (u'green', (0, 1, 0, 1)): [20], (u'', (0, 0.737095, 1, 1)): [8], (u'', (1, 0.421368, 0, 1)): [35], (u'', (1, 0.210884, 0, 1)): [37], (u'', (0.947179, 1, 0, 1)): [29],
(u'', (0, 1, 0.420968, 1)): [16], (u'', (0.420968, 1, 0, 1)): [24], (u'', (0, 0.0004, 1, 1)): [1], (u'', (0, 0.526611, 1, 1)): [6], (u'', (0.736695, 1, 0, 1)): [27], (u'', (0, 1, 0.526211, 1)): [15], (u'white', (1, 1, 1, 1)): [41], (u'', (0.841937, 1, 0, 1)): [28], (u'', (0.526211, 1, 0, 1)): [25]})
	viewerInfo = {'cameraAttrs': {'center': (9.4544999952316, -13.298000002384, 5.2841099803378), 'fieldOfView': 38.32586209521, 'nearFar': (38.733802977896, -28.16558301722), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 5.2604999880791}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'showShadows': False, 'viewSize': 41.703086343916, 'labelsOnTop': True, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 2, 'singleLayerTransparency': True, 'shadowTextureSize': 2048, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [('Chimera default', [(1, 1, 1, 1), (0, 0, 1, 1)], 1), 1, 0, 0], 'depthCue': True, 'highlight': 0, 'scaleFactor': 0.63154545749488, 'angleDependentTransparency': True, 'backgroundMethod': 0}, 'viewerHL': 20, 'cameraMode': 'mono', 'detail': 1.5, 'viewerFog': None, 'viewerBG': 41}

	replyobj.status("Initializing session restore...", blankAfter=0,
		secondary=True)
	from SimpleSession.versions.v64 import expandSummary
	init(dict(enumerate(expandSummary(colorInfo))))
	replyobj.status("Restoring colors...", blankAfter=0,
		secondary=True)
	restoreColors(colors, materials)
	replyobj.status("Restoring molecules...", blankAfter=0,
		secondary=True)
	restoreMolecules(molInfo, resInfo, atomInfo, bondInfo, crdInfo)
	replyobj.status("Restoring surfaces...", blankAfter=0,
		secondary=True)
	restoreSurfaces(surfInfo)
	replyobj.status("Restoring VRML models...", blankAfter=0,
		secondary=True)
	restoreVRML(vrmlInfo)
	replyobj.status("Restoring pseudobond groups...", blankAfter=0,
		secondary=True)
	restorePseudoBondGroups(pbInfo)
	replyobj.status("Restoring model associations...", blankAfter=0,
		secondary=True)
	restoreModelAssociations(modelAssociations)
	replyobj.status("Restoring camera...", blankAfter=0,
		secondary=True)
	restoreViewer(viewerInfo)

try:
	restoreCoreModels()
except:
	reportRestoreError("Error restoring core models")

	replyobj.status("Restoring extension info...", blankAfter=0,
		secondary=True)


try:
	import StructMeasure
	from StructMeasure.DistMonitor import restoreDistances
	registerAfterModelsCB(restoreDistances, 1)
except:
	reportRestoreError("Error restoring distances in session")


def restoreMidasBase():
	formattedPositions = {}
	import Midas
	Midas.restoreMidasBase(formattedPositions)
try:
	restoreMidasBase()
except:
	reportRestoreError('Error restoring Midas base state')


def restoreMidasText():
	from Midas import midas_text
	midas_text.aliases = {}
	midas_text.userSurfCategories = {}

try:
	restoreMidasText()
except:
	reportRestoreError('Error restoring Midas text state')


def restore_cap_attributes():
 cap_attributes = \
  {
   'cap_attributes': [
     {
      'cap_color': None,
      'class': 'Model_Capper_State',
      'display_style': None,
      'surface': ( 0, 0, ),
      'version': 1,
     },
    ],
   'cap_color': None,
   'cap_offset': 0.01,
   'class': 'Caps_State',
   'default_cap_offset': 0.01,
   'mesh_style': False,
   'shown': True,
   'subdivision_factor': 1.0,
   'version': 1,
  }
 import SurfaceCap.session
 SurfaceCap.session.restore_cap_attributes(cap_attributes)
registerAfterModelsCB(restore_cap_attributes)


def restore_volume_data():
 volume_data_state = \
  {
   'class': 'Volume_Manager_State',
   'data_and_regions_state': [ ],
   'version': 2,
  }
 from VolumeViewer import session
 session.restore_volume_data_state(volume_data_state)

try:
  restore_volume_data()
except:
  reportRestoreError('Error restoring volume data')

geomData = {'AxisManager': {}, 'CentroidManager': {}, 'PlaneManager': {}}

try:
	from StructMeasure.Geometry import geomManager
	geomManager._restoreSession(geomData)
except:
	reportRestoreError("Error restoring geometry objects in session")


def restoreSession_RibbonStyleEditor():
	import SimpleSession
	import RibbonStyleEditor
	userScalings = []
	userXSections = []
	userResidueClasses = []
	residueData = [(1, 'Chimera default', 'rounded', u'amino acid'), (2, 'Chimera default', 'rounded', u'amino acid'), (3, 'Chimera default', 'rounded', u'amino acid'), (4, 'Chimera default', 'rounded', u'amino acid'), (5, 'Chimera default', 'rounded', u'amino acid'), (6, 'Chimera default', 'rounded', u'amino acid'), (7, 'Chimera default', 'rounded', u'amino acid'), (8, 'Chimera default', 'rounded', u'amino acid'), (9, 'Chimera default', 'rounded', u'amino acid'), (10, 'Chimera default', 'rounded', u'amino acid'), (11, 'Chimera default', 'rounded', u'amino acid'), (12, 'Chimera default', 'rounded', u'amino acid'), (13, 'Chimera default', 'rounded', u'amino acid'), (14, 'Chimera default', 'rounded', u'amino acid'), (15, 'Chimera default', 'rounded', u'amino acid'), (16, 'Chimera default', 'rounded', u'amino acid'), (17, 'Chimera default', 'rounded', u'amino acid'), (18, 'Chimera default', 'rounded', u'amino acid'), (19, 'Chimera default', 'rounded', u'amino acid'), (20, 'Chimera default', 'rounded', u'amino acid'), (21, 'Chimera default', 'rounded', u'amino acid'), (22, 'Chimera default', 'rounded', u'amino acid'),
(23, 'Chimera default', 'rounded', u'amino acid'), (24, 'Chimera default', 'rounded', u'amino acid'), (25, 'Chimera default', 'rounded', u'amino acid'), (26, 'Chimera default', 'rounded', u'amino acid'), (27, 'Chimera default', 'rounded', u'amino acid'), (28, 'Chimera default', 'rounded', u'amino acid'), (29, 'Chimera default', 'rounded', u'amino acid'), (30, 'Chimera default', 'rounded', u'amino acid'), (31, 'Chimera default', 'rounded', u'amino acid'), (32, 'Chimera default', 'rounded', u'amino acid'), (33, 'Chimera default', 'rounded', u'amino acid'), (34, 'Chimera default', 'rounded', u'amino acid'), (35, 'Chimera default', 'rounded', u'amino acid'), (36, 'Chimera default', 'rounded', u'amino acid'), (37, 'Chimera default', 'rounded', u'amino acid'), (38, 'Chimera default', 'rounded', u'amino acid'), (39, 'Chimera default', 'rounded', u'amino acid')]
	flags = RibbonStyleEditor.NucleicDefault1
	SimpleSession.registerAfterModelsCB(RibbonStyleEditor.restoreState,
				(userScalings, userXSections,
				userResidueClasses, residueData, flags))
try:
	restoreSession_RibbonStyleEditor()
except:
	reportRestoreError("Error restoring RibbonStyleEditor state")

trPickle = 'gAJjQW5pbWF0ZS5UcmFuc2l0aW9ucwpUcmFuc2l0aW9ucwpxASmBcQJ9cQMoVQxjdXN0b21fc2NlbmVxBGNBbmltYXRlLlRyYW5zaXRpb24KVHJhbnNpdGlvbgpxBSmBcQZ9cQcoVQZmcmFtZXNxCEsBVQ1kaXNjcmV0ZUZyYW1lcQlLAVUKcHJvcGVydGllc3EKXXELVQNhbGxxDGFVBG5hbWVxDWgEVQRtb2RlcQ5VBmxpbmVhcnEPdWJVCGtleWZyYW1lcRBoBSmBcRF9cRIoaAhLFGgJSwFoCl1xE2gMYWgNaBBoDmgPdWJVBXNjZW5lcRRoBSmBcRV9cRYoaAhLAWgJSwFoCl1xF2gMYWgNaBRoDmgPdWJ1Yi4='
scPickle = 'gAJjQW5pbWF0ZS5TY2VuZXMKU2NlbmVzCnEBKYFxAn1xA1UHbWFwX2lkc3EEfXNiLg=='
kfPickle = 'gAJjQW5pbWF0ZS5LZXlmcmFtZXMKS2V5ZnJhbWVzCnEBKYFxAn1xA1UHZW50cmllc3EEXXEFc2Iu'
def restoreAnimation():
	'A method to unpickle and restore animation objects'
	# Scenes must be unpickled after restoring transitions, because each
	# scene links to a 'scene' transition. Likewise, keyframes must be 
	# unpickled after restoring scenes, because each keyframe links to a scene.
	# The unpickle process is left to the restore* functions, it's 
	# important that it doesn't happen prior to calling those functions.
	import SimpleSession
	from Animate.Session import restoreTransitions
	from Animate.Session import restoreScenes
	from Animate.Session import restoreKeyframes
	SimpleSession.registerAfterModelsCB(restoreTransitions, trPickle)
	SimpleSession.registerAfterModelsCB(restoreScenes, scPickle)
	SimpleSession.registerAfterModelsCB(restoreKeyframes, kfPickle)
try:
	restoreAnimation()
except:
	reportRestoreError('Error in Animate.Session')

def restoreLightController():
	import Lighting
	Lighting._setFromParams({'ratio': 1.25, 'brightness': 1.16, 'material': [30.0, (0.85, 0.85, 0.85), 1.0], 'back': [(0.35740674433659325, 0.6604015517481454, -0.6604015517481455), (1.0, 1.0, 1.0), 0.0], 'mode': 'ambient', 'key': [(-0.35740674433659325, 0.6604015517481454, 0.6604015517481455), (1.0, 1.0, 1.0), 1.0], 'contrast': 0.83, 'fill': [(0.25056280708573153, 0.25056280708573153, 0.9351131265310293), (1.0, 1.0, 1.0), 0.0]})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")


def restoreRemainder():
	from SimpleSession.versions.v64 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip, restoreSilhouettes

	curSelIds =  []
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 4 }
	windowSize = (1345, 618)
	xformMap = {0: (((0.024655953251818, -0.86528207267789, -0.50067855823023), 159.63898144217), (21.788361791395, -8.7346520978663, 16.319373417855), True)}
	fontInfo = {'face': ('Sans Serif', 'Normal', 16)}
	clipPlaneInfo = {}
	silhouettes = {0: True, 582: True, 583: True}

	replyobj.status("Restoring window...", blankAfter=0,
		secondary=True)
	restoreWindowSize(windowSize)
	replyobj.status("Restoring open states...", blankAfter=0,
		secondary=True)
	restoreOpenStates(xformMap)
	replyobj.status("Restoring font info...", blankAfter=0,
		secondary=True)
	restoreFontInfo(fontInfo)
	replyobj.status("Restoring selections...", blankAfter=0,
		secondary=True)
	restoreSelections(curSelIds, savedSels)
	replyobj.status("Restoring openModel attributes...", blankAfter=0,
		secondary=True)
	restoreOpenModelsAttrs(openModelsAttrs)
	replyobj.status("Restoring model clipping...", blankAfter=0,
		secondary=True)
	restoreModelClip(clipPlaneInfo)
	replyobj.status("Restoring per-model silhouettes...", blankAfter=0,
		secondary=True)
	restoreSilhouettes(silhouettes)

	replyobj.status("Restoring remaining extension info...", blankAfter=0,
		secondary=True)
try:
	restoreRemainder()
except:
	reportRestoreError("Error restoring post-model state")
from SimpleSession.versions.v64 import makeAfterModelsCBs
makeAfterModelsCBs()

from SimpleSession.versions.v64 import endRestore
replyobj.status('Finishing restore...', blankAfter=0, secondary=True)
endRestore({})
replyobj.status('', secondary=True)
replyobj.status('Restore finished.')


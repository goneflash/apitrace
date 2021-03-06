##########################################################################
#
# Copyright 2008-2009 VMware, Inc.
# All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
##########################################################################/

"""d3dtypes.h"""

from winapi import *

D3DVALUE = Float
LPD3DVALUE = Pointer(D3DVALUE)

D3DFIXED = LONG

LPD3DVALIDATECALLBACK = Opaque("LPD3DVALIDATECALLBACK")
LPD3DENUMTEXTUREFORMATSCALLBACK = Opaque("LPD3DENUMTEXTUREFORMATSCALLBACK")
LPD3DENUMPIXELFORMATSCALLBACK = Opaque("LPD3DENUMPIXELFORMATSCALLBACK")

D3DCOLOR = Alias("D3DCOLOR", DWORD)

D3DVECTOR = Struct("D3DVECTOR", [
    (D3DVALUE, "x"),
    (D3DVALUE, "y"),
    (D3DVALUE, "z"),
])
LPD3DVECTOR = Pointer(D3DVECTOR)

D3DCOLORVALUE = Struct("D3DCOLORVALUE", [
    (D3DVALUE, "r"),
    (D3DVALUE, "g"),
    (D3DVALUE, "b"),
    (D3DVALUE, "a"),
])
LPD3DCOLORVALUE = Pointer(D3DCOLORVALUE)

D3DRECT = Struct("D3DRECT", [
    (LONG, "x1"),
    (LONG, "y1"),
    (LONG, "x2"),
    (LONG, "y2"),
])
LPD3DRECT = Pointer(D3DRECT)

D3DMATERIALHANDLE = DWORD
LPD3DMATERIALHANDLE = Pointer(D3DMATERIALHANDLE)

D3DTEXTUREHANDLE = DWORD
LPD3DTEXTUREHANDLE = Pointer(D3DTEXTUREHANDLE)

D3DMATRIXHANDLE = DWORD
LPD3DMATRIXHANDLE = Pointer(D3DMATRIXHANDLE)

D3DHVERTEX = Struct("D3DHVERTEX", [
    (DWORD, "dwFlags"),
    (D3DVALUE, "hx"),
    (D3DVALUE, "hy"),
    (D3DVALUE, "hz"),
])
LPD3DHVERTEX = Pointer(D3DHVERTEX)

D3DTLVERTEX = Struct("D3DTLVERTEX", [
    (D3DVALUE, "sx"),
    (D3DVALUE, "sy"),
    (D3DVALUE, "sz"),
    (D3DVALUE, "rhw"),
    (D3DCOLOR, "color"),
    (D3DCOLOR, "specular"),
    (D3DVALUE, "tu"),
    (D3DVALUE, "tv"),
])
LPD3DTLVERTEX = Pointer(D3DTLVERTEX)

D3DLVERTEX = Struct("D3DLVERTEX", [
    (D3DVALUE, "x"),
    (D3DVALUE, "y"),
    (D3DVALUE, "z"),
    (DWORD, "dwReserved"),
    (D3DCOLOR, "color"),
    (D3DCOLOR, "specular"),
    (D3DVALUE, "tu"),
    (D3DVALUE, "tv"),
])
LPD3DLVERTEX = Pointer(D3DLVERTEX)

D3DVERTEX = Struct("D3DVERTEX", [
    (D3DVALUE, "x"),
    (D3DVALUE, "y"),
    (D3DVALUE, "z"),
    (D3DVALUE, "nx"),
    (D3DVALUE, "ny"),
    (D3DVALUE, "nz"),
    (D3DVALUE, "tu"),
    (D3DVALUE, "tv"),
])
LPD3DVERTEX = Pointer(D3DVERTEX)

D3DMATRIX = Struct("D3DMATRIX", [
    (D3DVALUE, "_%u" % index) for index in [
         11, 12, 13, 14,
         21, 22, 23, 24,
         31, 32, 33, 34,
         41, 42, 43, 44
    ]
])
LPD3DMATRIX = Alias("LPD3DMATRIX", Pointer(D3DMATRIX))

D3DVIEWPORT = Struct("D3DVIEWPORT", [
    (DWORD, "dwSize"),
    (DWORD, "dwX"),
    (DWORD, "dwY"),
    (DWORD, "dwWidth"),
    (DWORD, "dwHeight"),
    (D3DVALUE, "dvScaleX"),
    (D3DVALUE, "dvScaleY"),
    (D3DVALUE, "dvMaxX"),
    (D3DVALUE, "dvMaxY"),
    (D3DVALUE, "dvMinZ"),
    (D3DVALUE, "dvMaxZ"),
])
LPD3DVIEWPORT = Pointer(D3DVIEWPORT)

D3DVIEWPORT2 = Struct("D3DVIEWPORT2", [
    (DWORD, "dwSize"),
    (DWORD, "dwX"),
    (DWORD, "dwY"),
    (DWORD, "dwWidth"),
    (DWORD, "dwHeight"),
    (D3DVALUE, "dvClipX"),
    (D3DVALUE, "dvClipY"),
    (D3DVALUE, "dvClipWidth"),
    (D3DVALUE, "dvClipHeight"),
    (D3DVALUE, "dvMinZ"),
    (D3DVALUE, "dvMaxZ"),
])
LPD3DVIEWPORT2 = Pointer(D3DVIEWPORT2)

D3DVIEWPORT7 = Struct("D3DVIEWPORT7", [
    (DWORD, "dwX"),
    (DWORD, "dwY"),
    (DWORD, "dwWidth"),
    (DWORD, "dwHeight"),
    (D3DVALUE, "dvMinZ"),
    (D3DVALUE, "dvMaxZ"),
])
LPD3DVIEWPORT7 = Pointer(D3DVIEWPORT7)

D3DCLIP = Flags(DWORD, [
    "D3DCLIP_LEFT",
    "D3DCLIP_RIGHT",
    "D3DCLIP_TOP",
    "D3DCLIP_BOTTOM",
    "D3DCLIP_FRONT",
    "D3DCLIP_BACK",
    "D3DCLIP_GEN0",
    "D3DCLIP_GEN1",
    "D3DCLIP_GEN2",
    "D3DCLIP_GEN3",
    "D3DCLIP_GEN4",
    "D3DCLIP_GEN5",
])

D3DSTATUS = Flags(DWORD, [
    "D3DSTATUS_DEFAULT",
    "D3DSTATUS_CLIPUNIONALL",
    "D3DSTATUS_CLIPUNIONLEFT",
    "D3DSTATUS_CLIPUNIONRIGHT",
    "D3DSTATUS_CLIPUNIONTOP",
    "D3DSTATUS_CLIPUNIONBOTTOM",
    "D3DSTATUS_CLIPUNIONFRONT",
    "D3DSTATUS_CLIPUNIONBACK",
    "D3DSTATUS_CLIPUNIONGEN0",
    "D3DSTATUS_CLIPUNIONGEN1",
    "D3DSTATUS_CLIPUNIONGEN2",
    "D3DSTATUS_CLIPUNIONGEN3",
    "D3DSTATUS_CLIPUNIONGEN4",
    "D3DSTATUS_CLIPUNIONGEN5",
    "D3DSTATUS_CLIPINTERSECTIONALL",
    "D3DSTATUS_CLIPINTERSECTIONLEFT",
    "D3DSTATUS_CLIPINTERSECTIONRIGHT",
    "D3DSTATUS_CLIPINTERSECTIONTOP",
    "D3DSTATUS_CLIPINTERSECTIONBOTTOM",
    "D3DSTATUS_CLIPINTERSECTIONFRONT",
    "D3DSTATUS_CLIPINTERSECTIONBACK",
    "D3DSTATUS_CLIPINTERSECTIONGEN0",
    "D3DSTATUS_CLIPINTERSECTIONGEN1",
    "D3DSTATUS_CLIPINTERSECTIONGEN2",
    "D3DSTATUS_CLIPINTERSECTIONGEN3",
    "D3DSTATUS_CLIPINTERSECTIONGEN4",
    "D3DSTATUS_CLIPINTERSECTIONGEN5",
    "D3DSTATUS_ZNOTVISIBLE",
])

D3DTRANSFORM = Flags(DWORD, [
    "D3DTRANSFORM_CLIPPED",
    "D3DTRANSFORM_UNCLIPPED",
])

D3DTRANSFORMDATA = Struct("D3DTRANSFORMDATA", [
    (DWORD, "dwSize"),
    (LPVOID, "lpIn"),
    (DWORD, "dwInSize"),
    (LPVOID, "lpOut"),
    (DWORD, "dwOutSize"),
    (LPD3DHVERTEX, "lpHOut"),
    (DWORD, "dwClip"),
    (DWORD, "dwClipIntersection"),
    (DWORD, "dwClipUnion"),
    (D3DRECT, "drExtent"),
])
LPD3DTRANSFORMDATA = Pointer(D3DTRANSFORMDATA)

D3DLIGHTINGELEMENT = Struct("D3DLIGHTINGELEMENT", [
    (D3DVECTOR, "dvPosition"),
    (D3DVECTOR, "dvNormal"),
])
LPD3DLIGHTINGELEMENT = Pointer(D3DLIGHTINGELEMENT)

D3DMATERIAL = Struct("D3DMATERIAL", [
    (DWORD, "dwSize"),
    (D3DCOLORVALUE, "diffuse"),
    (D3DCOLORVALUE, "ambient"),
    (D3DCOLORVALUE, "specular"),
    (D3DCOLORVALUE, "emissive"),
    (D3DVALUE, "power"),
    (D3DTEXTUREHANDLE, "hTexture"),
    (DWORD, "dwRampSize"),
])
LPD3DMATERIAL = Pointer(D3DMATERIAL)

D3DMATERIAL7 = Struct("D3DMATERIAL7", [
    (D3DCOLORVALUE, "diffuse"),
    (D3DCOLORVALUE, "ambient"),
    (D3DCOLORVALUE, "specular"),
    (D3DCOLORVALUE, "emissive"),
    (D3DVALUE, "power"),
])
LPD3DMATERIAL7 = Pointer(D3DMATERIAL7)

D3DLIGHTTYPE = Enum("D3DLIGHTTYPE", [
    "D3DLIGHT_POINT",
    "D3DLIGHT_SPOT",
    "D3DLIGHT_DIRECTIONAL",
    "D3DLIGHT_PARALLELPOINT",
    "D3DLIGHT_GLSPOT",
])

D3DLIGHT = Struct("D3DLIGHT", [
    (DWORD, "dwSize"),
    (D3DLIGHTTYPE, "dltType"),
    (D3DCOLORVALUE, "dcvColor"),
    (D3DVECTOR, "dvPosition"),
    (D3DVECTOR, "dvDirection"),
    (D3DVALUE, "dvRange"),
    (D3DVALUE, "dvFalloff"),
    (D3DVALUE, "dvAttenuation0"),
    (D3DVALUE, "dvAttenuation1"),
    (D3DVALUE, "dvAttenuation2"),
    (D3DVALUE, "dvTheta"),
    (D3DVALUE, "dvPhi"),
])
LPD3DLIGHT = Pointer(D3DLIGHT)

D3DLIGHT7 = Struct("D3DLIGHT7", [
    (D3DLIGHTTYPE, "dltType"),
    (D3DCOLORVALUE, "dcvDiffuse"),
    (D3DCOLORVALUE, "dcvSpecular"),
    (D3DCOLORVALUE, "dcvAmbient"),
    (D3DVECTOR, "dvPosition"),
    (D3DVECTOR, "dvDirection"),
    (D3DVALUE, "dvRange"),
    (D3DVALUE, "dvFalloff"),
    (D3DVALUE, "dvAttenuation0"),
    (D3DVALUE, "dvAttenuation1"),
    (D3DVALUE, "dvAttenuation2"),
    (D3DVALUE, "dvTheta"),
    (D3DVALUE, "dvPhi"),
])
LPD3DLIGHT7 = Pointer(D3DLIGHT7)

D3DLIGHTFLAGS = Flags(DWORD, [
    "D3DLIGHT_ACTIVE",
    "D3DLIGHT_NO_SPECULAR",
    "D3DLIGHT_ALL",
])

D3DLIGHT2 = Struct("D3DLIGHT2", [
    (DWORD, "dwSize"),
    (D3DLIGHTTYPE, "dltType"),
    (D3DCOLORVALUE, "dcvColor"),
    (D3DVECTOR, "dvPosition"),
    (D3DVECTOR, "dvDirection"),
    (D3DVALUE, "dvRange"),
    (D3DVALUE, "dvFalloff"),
    (D3DVALUE, "dvAttenuation0"),
    (D3DVALUE, "dvAttenuation1"),
    (D3DVALUE, "dvAttenuation2"),
    (D3DVALUE, "dvTheta"),
    (D3DVALUE, "dvPhi"),
    (DWORD, "dwFlags"),
])
LPD3DLIGHT2 = Pointer(D3DLIGHT2)

D3DLIGHTDATA = Struct("D3DLIGHTDATA", [
    (DWORD, "dwSize"),
    (LPD3DLIGHTINGELEMENT, "lpIn"),
    (DWORD, "dwInSize"),
    (LPD3DTLVERTEX, "lpOut"),
    (DWORD, "dwOutSize"),
])
LPD3DLIGHTDATA = Pointer(D3DLIGHTDATA)

D3DCOLORMODEL = FakeEnum(DWORD, [
    "D3DCOLOR_MONO",
    "D3DCOLOR_RGB",
])

D3DCLEAR = Flags(DWORD, [
    "D3DCLEAR_TARGET",
    "D3DCLEAR_ZBUFFER",
    "D3DCLEAR_STENCIL",
])

D3DOPCODE = Enum("D3DOPCODE", [
    "D3DOP_POINT",
    "D3DOP_LINE",
    "D3DOP_TRIANGLE",
    "D3DOP_MATRIXLOAD",
    "D3DOP_MATRIXMULTIPLY",
    "D3DOP_STATETRANSFORM",
    "D3DOP_STATELIGHT",
    "D3DOP_STATERENDER",
    "D3DOP_PROCESSVERTICES",
    "D3DOP_TEXTURELOAD",
    "D3DOP_EXIT",
    "D3DOP_BRANCHFORWARD",
    "D3DOP_SPAN",
    "D3DOP_SETSTATUS",
])

D3DINSTRUCTION = Struct("D3DINSTRUCTION", [
    (BYTE, "bOpcode"),
    (BYTE, "bSize"),
    (WORD, "wCount"),
])

D3DTEXTURELOAD = Struct("D3DTEXTURELOAD", [
    (D3DTEXTUREHANDLE, "hDestTexture"),
    (D3DTEXTUREHANDLE, "hSrcTexture"),
])

D3DPICKRECORD = Struct("D3DPICKRECORD", [
    (BYTE, "bOpcode"),
    (BYTE, "bPad"),
    (DWORD, "dwOffset"),
    (D3DVALUE, "dvZ"),
])
LPD3DPICKRECORD = Pointer(D3DPICKRECORD)

D3DSHADEMODE = Enum("D3DSHADEMODE", [
    "D3DSHADE_FLAT",
    "D3DSHADE_GOURAUD",
    "D3DSHADE_PHONG",
])

D3DFILLMODE = Enum("D3DFILLMODE", [
    "D3DFILL_POINT",
    "D3DFILL_WIREFRAME",
    "D3DFILL_SOLID",
])

D3DLINEPATTERN = Struct("D3DLINEPATTERN", [
    (WORD, "wRepeatFactor"),
    (WORD, "wLinePattern"),
])

D3DTEXTUREFILTER = Enum("D3DTEXTUREFILTER", [
    "D3DFILTER_NEAREST",
    "D3DFILTER_LINEAR",
    "D3DFILTER_MIPNEAREST",
    "D3DFILTER_MIPLINEAR",
    "D3DFILTER_LINEARMIPNEAREST",
    "D3DFILTER_LINEARMIPLINEAR",
])

D3DBLEND = Enum("D3DBLEND", [
    "D3DBLEND_ZERO",
    "D3DBLEND_ONE",
    "D3DBLEND_SRCCOLOR",
    "D3DBLEND_INVSRCCOLOR",
    "D3DBLEND_SRCALPHA",
    "D3DBLEND_INVSRCALPHA",
    "D3DBLEND_DESTALPHA",
    "D3DBLEND_INVDESTALPHA",
    "D3DBLEND_DESTCOLOR",
    "D3DBLEND_INVDESTCOLOR",
    "D3DBLEND_SRCALPHASAT",
    "D3DBLEND_BOTHSRCALPHA",
    "D3DBLEND_BOTHINVSRCALPHA",
])

D3DTEXTUREBLEND = Enum("D3DTEXTUREBLEND", [
    "D3DTBLEND_DECAL",
    "D3DTBLEND_MODULATE",
    "D3DTBLEND_DECALALPHA",
    "D3DTBLEND_MODULATEALPHA",
    "D3DTBLEND_DECALMASK",
    "D3DTBLEND_MODULATEMASK",
    "D3DTBLEND_COPY",
    "D3DTBLEND_ADD",
])

D3DTEXTUREADDRESS = Enum("D3DTEXTUREADDRESS", [
    "D3DTADDRESS_WRAP",
    "D3DTADDRESS_MIRROR",
    "D3DTADDRESS_CLAMP",
    "D3DTADDRESS_BORDER",
])

D3DCULL = Enum("D3DCULL", [
    "D3DCULL_NONE",
    "D3DCULL_CW",
    "D3DCULL_CCW",
])

D3DCMPFUNC = Enum("D3DCMPFUNC", [
    "D3DCMP_NEVER",
    "D3DCMP_LESS",
    "D3DCMP_EQUAL",
    "D3DCMP_LESSEQUAL",
    "D3DCMP_GREATER",
    "D3DCMP_NOTEQUAL",
    "D3DCMP_GREATEREQUAL",
    "D3DCMP_ALWAYS",
])

D3DSTENCILOP = Enum("D3DSTENCILOP", [
    "D3DSTENCILOP_KEEP",
    "D3DSTENCILOP_ZERO",
    "D3DSTENCILOP_REPLACE",
    "D3DSTENCILOP_INCRSAT",
    "D3DSTENCILOP_DECRSAT",
    "D3DSTENCILOP_INVERT",
    "D3DSTENCILOP_INCR",
    "D3DSTENCILOP_DECR",
])

D3DFOGMODE = Enum("D3DFOGMODE", [
    "D3DFOG_NONE",
    "D3DFOG_EXP",
    "D3DFOG_EXP2",
    "D3DFOG_LINEAR",
])

D3DZBUFFERTYPE = Enum("D3DZBUFFERTYPE", [
    "D3DZB_FALSE",
    "D3DZB_TRUE",
    "D3DZB_USEW",
])

D3DANTIALIASMODE = Enum("D3DANTIALIASMODE", [
    "D3DANTIALIAS_NONE",
    "D3DANTIALIAS_SORTDEPENDENT",
    "D3DANTIALIAS_SORTINDEPENDENT",
])

D3DVERTEXTYPE = Enum("D3DVERTEXTYPE", [
    "D3DVT_VERTEX",
    "D3DVT_LVERTEX",
    "D3DVT_TLVERTEX",
])

D3DPRIMITIVETYPE = Enum("D3DPRIMITIVETYPE", [
    "D3DPT_POINTLIST",
    "D3DPT_LINELIST",
    "D3DPT_LINESTRIP",
    "D3DPT_TRIANGLELIST",
    "D3DPT_TRIANGLESTRIP",
    "D3DPT_TRIANGLEFAN",
])

D3DTRANSFORMSTATETYPE = Enum("D3DTRANSFORMSTATETYPE", [
    "D3DTRANSFORMSTATE_WORLD",
    "D3DTRANSFORMSTATE_VIEW",
    "D3DTRANSFORMSTATE_PROJECTION",
    "D3DTRANSFORMSTATE_WORLD1",
    "D3DTRANSFORMSTATE_WORLD2",
    "D3DTRANSFORMSTATE_WORLD3",
    "D3DTRANSFORMSTATE_TEXTURE0",
    "D3DTRANSFORMSTATE_TEXTURE1",
    "D3DTRANSFORMSTATE_TEXTURE2",
    "D3DTRANSFORMSTATE_TEXTURE3",
    "D3DTRANSFORMSTATE_TEXTURE4",
    "D3DTRANSFORMSTATE_TEXTURE5",
    "D3DTRANSFORMSTATE_TEXTURE6",
    "D3DTRANSFORMSTATE_TEXTURE7",
])

D3DLIGHTSTATETYPE = Enum("D3DLIGHTSTATETYPE", [
    "D3DLIGHTSTATE_MATERIAL",
    "D3DLIGHTSTATE_AMBIENT",
    "D3DLIGHTSTATE_COLORMODEL",
    "D3DLIGHTSTATE_FOGMODE",
    "D3DLIGHTSTATE_FOGSTART",
    "D3DLIGHTSTATE_FOGEND",
    "D3DLIGHTSTATE_FOGDENSITY",
    "D3DLIGHTSTATE_COLORVERTEX",
])

D3DMATERIALCOLORSOURCE = Enum("D3DMATERIALCOLORSOURCE", [
    "D3DMCS_MATERIAL",
    "D3DMCS_COLOR1",
    "D3DMCS_COLOR2",
])

D3DWRAPCOORD = Flags(DWORD, [
    "D3DWRAPCOORD_0",
    "D3DWRAPCOORD_1",
    "D3DWRAPCOORD_2",
    "D3DWRAPCOORD_3",
])

D3DRENDERSTATETYPE = Enum("D3DRENDERSTATETYPE", [
    "D3DRENDERSTATE_ANTIALIAS",
    "D3DRENDERSTATE_TEXTUREPERSPECTIVE",
    "D3DRENDERSTATE_ZENABLE",
    "D3DRENDERSTATE_FILLMODE",
    "D3DRENDERSTATE_SHADEMODE",
    "D3DRENDERSTATE_LINEPATTERN",
    "D3DRENDERSTATE_ZWRITEENABLE",
    "D3DRENDERSTATE_ALPHATESTENABLE",
    "D3DRENDERSTATE_LASTPIXEL",
    "D3DRENDERSTATE_SRCBLEND",
    "D3DRENDERSTATE_DESTBLEND",
    "D3DRENDERSTATE_CULLMODE",
    "D3DRENDERSTATE_ZFUNC",
    "D3DRENDERSTATE_ALPHAREF",
    "D3DRENDERSTATE_ALPHAFUNC",
    "D3DRENDERSTATE_DITHERENABLE",
    "D3DRENDERSTATE_ALPHABLENDENABLE",
    "D3DRENDERSTATE_FOGENABLE",
    "D3DRENDERSTATE_SPECULARENABLE",
    "D3DRENDERSTATE_ZVISIBLE",
    "D3DRENDERSTATE_STIPPLEDALPHA",
    "D3DRENDERSTATE_FOGCOLOR",
    "D3DRENDERSTATE_FOGTABLEMODE",
    "D3DRENDERSTATE_FOGSTART",
    "D3DRENDERSTATE_FOGEND",
    "D3DRENDERSTATE_FOGDENSITY",
    "D3DRENDERSTATE_EDGEANTIALIAS",
    "D3DRENDERSTATE_COLORKEYENABLE",
    "D3DRENDERSTATE_ZBIAS",
    "D3DRENDERSTATE_RANGEFOGENABLE",
    "D3DRENDERSTATE_STENCILENABLE",
    "D3DRENDERSTATE_STENCILFAIL",
    "D3DRENDERSTATE_STENCILZFAIL",
    "D3DRENDERSTATE_STENCILPASS",
    "D3DRENDERSTATE_STENCILFUNC",
    "D3DRENDERSTATE_STENCILREF",
    "D3DRENDERSTATE_STENCILMASK",
    "D3DRENDERSTATE_STENCILWRITEMASK",
    "D3DRENDERSTATE_TEXTUREFACTOR",
    "D3DRENDERSTATE_WRAP0",
    "D3DRENDERSTATE_WRAP1",
    "D3DRENDERSTATE_WRAP2",
    "D3DRENDERSTATE_WRAP3",
    "D3DRENDERSTATE_WRAP4",
    "D3DRENDERSTATE_WRAP5",
    "D3DRENDERSTATE_WRAP6",
    "D3DRENDERSTATE_WRAP7",
    "D3DRENDERSTATE_CLIPPING",
    "D3DRENDERSTATE_LIGHTING",
    "D3DRENDERSTATE_EXTENTS",
    "D3DRENDERSTATE_AMBIENT",
    "D3DRENDERSTATE_FOGVERTEXMODE",
    "D3DRENDERSTATE_COLORVERTEX",
    "D3DRENDERSTATE_LOCALVIEWER",
    "D3DRENDERSTATE_NORMALIZENORMALS",
    "D3DRENDERSTATE_COLORKEYBLENDENABLE",
    "D3DRENDERSTATE_DIFFUSEMATERIALSOURCE",
    "D3DRENDERSTATE_SPECULARMATERIALSOURCE",
    "D3DRENDERSTATE_AMBIENTMATERIALSOURCE",
    "D3DRENDERSTATE_EMISSIVEMATERIALSOURCE",
    "D3DRENDERSTATE_VERTEXBLEND",
    "D3DRENDERSTATE_CLIPPLANEENABLE",
    "D3DRENDERSTATE_TEXTUREHANDLE",
    "D3DRENDERSTATE_TEXTUREADDRESS",
    "D3DRENDERSTATE_WRAPU",
    "D3DRENDERSTATE_WRAPV",
    "D3DRENDERSTATE_MONOENABLE",
    "D3DRENDERSTATE_ROP2",
    "D3DRENDERSTATE_PLANEMASK",
    "D3DRENDERSTATE_TEXTUREMAG",
    "D3DRENDERSTATE_TEXTUREMIN",
    "D3DRENDERSTATE_TEXTUREMAPBLEND",
    "D3DRENDERSTATE_SUBPIXEL",
    "D3DRENDERSTATE_SUBPIXELX",
    "D3DRENDERSTATE_STIPPLEENABLE",
    "D3DRENDERSTATE_BORDERCOLOR",
    "D3DRENDERSTATE_TEXTUREADDRESSU",
    "D3DRENDERSTATE_TEXTUREADDRESSV",
    "D3DRENDERSTATE_MIPMAPLODBIAS",
    "D3DRENDERSTATE_ANISOTROPY",
    "D3DRENDERSTATE_FLUSHBATCH",
    "D3DRENDERSTATE_TRANSLUCENTSORTINDEPENDENT",
    "D3DRENDERSTATE_STIPPLEPATTERN00",
    "D3DRENDERSTATE_STIPPLEPATTERN01",
    "D3DRENDERSTATE_STIPPLEPATTERN02",
    "D3DRENDERSTATE_STIPPLEPATTERN03",
    "D3DRENDERSTATE_STIPPLEPATTERN04",
    "D3DRENDERSTATE_STIPPLEPATTERN05",
    "D3DRENDERSTATE_STIPPLEPATTERN06",
    "D3DRENDERSTATE_STIPPLEPATTERN07",
    "D3DRENDERSTATE_STIPPLEPATTERN08",
    "D3DRENDERSTATE_STIPPLEPATTERN09",
    "D3DRENDERSTATE_STIPPLEPATTERN10",
    "D3DRENDERSTATE_STIPPLEPATTERN11",
    "D3DRENDERSTATE_STIPPLEPATTERN12",
    "D3DRENDERSTATE_STIPPLEPATTERN13",
    "D3DRENDERSTATE_STIPPLEPATTERN14",
    "D3DRENDERSTATE_STIPPLEPATTERN15",
    "D3DRENDERSTATE_STIPPLEPATTERN16",
    "D3DRENDERSTATE_STIPPLEPATTERN17",
    "D3DRENDERSTATE_STIPPLEPATTERN18",
    "D3DRENDERSTATE_STIPPLEPATTERN19",
    "D3DRENDERSTATE_STIPPLEPATTERN20",
    "D3DRENDERSTATE_STIPPLEPATTERN21",
    "D3DRENDERSTATE_STIPPLEPATTERN22",
    "D3DRENDERSTATE_STIPPLEPATTERN23",
    "D3DRENDERSTATE_STIPPLEPATTERN24",
    "D3DRENDERSTATE_STIPPLEPATTERN25",
    "D3DRENDERSTATE_STIPPLEPATTERN26",
    "D3DRENDERSTATE_STIPPLEPATTERN27",
    "D3DRENDERSTATE_STIPPLEPATTERN28",
    "D3DRENDERSTATE_STIPPLEPATTERN29",
    "D3DRENDERSTATE_STIPPLEPATTERN30",
    "D3DRENDERSTATE_STIPPLEPATTERN31",
])

D3DSTATE = Struct("D3DSTATE", [
    (D3DTRANSFORMSTATETYPE, "dtstTransformStateType"),
    (D3DLIGHTSTATETYPE, "dlstLightStateType"),
    (D3DRENDERSTATETYPE, "drstRenderStateType"),
    (Array(DWORD, 1), "dwArg"),
    (Array(D3DVALUE, 1), "dvArg"),
])

D3DMATRIXLOAD = Struct("D3DMATRIXLOAD", [
    (D3DMATRIXHANDLE, "hDestMatrix"),
    (D3DMATRIXHANDLE, "hSrcMatrix"),
])

D3DMATRIXMULTIPLY = Struct("D3DMATRIXMULTIPLY", [
    (D3DMATRIXHANDLE, "hDestMatrix"),
    (D3DMATRIXHANDLE, "hSrcMatrix1"),
    (D3DMATRIXHANDLE, "hSrcMatrix2"),
])

D3DPROCESSVERTICES = Struct("D3DPROCESSVERTICES", [
    (DWORD, "dwFlags"),
    (WORD, "wStart"),
    (WORD, "wDest"),
    (DWORD, "dwCount"),
    (DWORD, "dwReserved"),
])

D3DPROCESSVERTICES = Flags(DWORD, [
    "D3DPROCESSVERTICES_TRANSFORMLIGHT",
    "D3DPROCESSVERTICES_TRANSFORM",
    "D3DPROCESSVERTICES_COPY",
    "D3DPROCESSVERTICES_OPMASK",
    "D3DPROCESSVERTICES_UPDATEEXTENTS",
    "D3DPROCESSVERTICES_NOCOLOR",
])

D3DTEXTURESTAGESTATETYPE = Enum("D3DTEXTURESTAGESTATETYPE", [
    "D3DTSS_COLOROP",
    "D3DTSS_COLORARG1",
    "D3DTSS_COLORARG2",
    "D3DTSS_ALPHAOP",
    "D3DTSS_ALPHAARG1",
    "D3DTSS_ALPHAARG2",
    "D3DTSS_BUMPENVMAT00",
    "D3DTSS_BUMPENVMAT01",
    "D3DTSS_BUMPENVMAT10",
    "D3DTSS_BUMPENVMAT11",
    "D3DTSS_TEXCOORDINDEX",
    "D3DTSS_ADDRESS",
    "D3DTSS_ADDRESSU",
    "D3DTSS_ADDRESSV",
    "D3DTSS_BORDERCOLOR",
    "D3DTSS_MAGFILTER",
    "D3DTSS_MINFILTER",
    "D3DTSS_MIPFILTER",
    "D3DTSS_MIPMAPLODBIAS",
    "D3DTSS_MAXMIPLEVEL",
    "D3DTSS_MAXANISOTROPY",
    "D3DTSS_BUMPENVLSCALE",
    "D3DTSS_BUMPENVLOFFSET",
    "D3DTSS_TEXTURETRANSFORMFLAGS",
])

D3DTSS_TCI = Flags(DWORD, [
    "D3DTSS_TCI_PASSTHRU",
    "D3DTSS_TCI_CAMERASPACENORMAL",
    "D3DTSS_TCI_CAMERASPACEPOSITION",
    "D3DTSS_TCI_CAMERASPACEREFLECTIONVECTOR",
])

D3DTEXTUREOP = Enum("D3DTEXTUREOP", [
    "D3DTOP_DISABLE",
    "D3DTOP_SELECTARG1",
    "D3DTOP_SELECTARG2",
    "D3DTOP_MODULATE",
    "D3DTOP_MODULATE2X",
    "D3DTOP_MODULATE4X",
    "D3DTOP_ADD",
    "D3DTOP_ADDSIGNED",
    "D3DTOP_ADDSIGNED2X",
    "D3DTOP_SUBTRACT",
    "D3DTOP_ADDSMOOTH",
    "D3DTOP_BLENDDIFFUSEALPHA",
    "D3DTOP_BLENDTEXTUREALPHA",
    "D3DTOP_BLENDFACTORALPHA",
    "D3DTOP_BLENDTEXTUREALPHAPM",
    "D3DTOP_BLENDCURRENTALPHA",
    "D3DTOP_PREMODULATE",
    "D3DTOP_MODULATEALPHA_ADDCOLOR",
    "D3DTOP_MODULATECOLOR_ADDALPHA",
    "D3DTOP_MODULATEINVALPHA_ADDCOLOR",
    "D3DTOP_MODULATEINVCOLOR_ADDALPHA",
    "D3DTOP_BUMPENVMAP",
    "D3DTOP_BUMPENVMAPLUMINANCE",
    "D3DTOP_DOTPRODUCT3",
])

# XXX: Actually a mixture of enums and flags
D3DTA = FakeEnum(DWORD, [
    "D3DTA_DIFFUSE",
    "D3DTA_CURRENT",
    "D3DTA_TEXTURE",
    "D3DTA_TFACTOR",
    "D3DTA_SPECULAR",
    #"D3DTA_COMPLEMENT",
    #"D3DTA_ALPHAREPLICATE",
])

D3DTEXTUREMAGFILTER = Enum("D3DTEXTUREMAGFILTER", [
    "D3DTFG_POINT",
    "D3DTFG_LINEAR",
    "D3DTFG_FLATCUBIC",
    "D3DTFG_GAUSSIANCUBIC",
    "D3DTFG_ANISOTROPIC",
])

D3DTEXTUREMINFILTER = Enum("D3DTEXTUREMINFILTER", [
    "D3DTFN_POINT",
    "D3DTFN_LINEAR",
    "D3DTFN_ANISOTROPIC",
])

D3DTEXTUREMIPFILTER = Enum("D3DTEXTUREMIPFILTER", [
    "D3DTFP_NONE",
    "D3DTFP_POINT",
    "D3DTFP_LINEAR",
])

D3DTRIFLAG = Flags(DWORD, [
    "D3DTRIFLAG_START",
    "D3DTRIFLAG_STARTFLAT(len)",
    "D3DTRIFLAG_ODD",
    "D3DTRIFLAG_EVEN",
    "D3DTRIFLAG_EDGEENABLETRIANGLE",
    "D3DTRIFLAG_EDGEENABLE1",
    "D3DTRIFLAG_EDGEENABLE2",
    "D3DTRIFLAG_EDGEENABLE3",
])

D3DTRIANGLE = Struct("D3DTRIANGLE", [
    (WORD, "v1"),
    (WORD, "v2"),
    (WORD, "v3"),
    (WORD, "wFlags"),
])

D3DLINE = Struct("D3DLINE", [
    (WORD, "v1"),
    (WORD, "v2"),
])

D3DSPAN = Struct("D3DSPAN", [
    (WORD, "wCount"),
    (WORD, "wFirst"),
])

D3DPOINT = Struct("D3DPOINT", [
    (WORD, "wCount"),
    (WORD, "wFirst"),
])

D3DBRANCH = Struct("D3DBRANCH", [
    (DWORD, "dwMask"),
    (DWORD, "dwValue"),
    (BOOL, "bNegate"),
    (DWORD, "dwOffset"),
])

D3DSTATUS = Struct("D3DSTATUS", [
    (DWORD, "dwFlags"),
    (DWORD, "dwStatus"),
    (D3DRECT, "drExtent"),
])

D3DSETSTATUS = Flags(DWORD, [
    "D3DSETSTATUS_STATUS",
    "D3DSETSTATUS_EXTENTS",
    "D3DSETSTATUS_ALL",
])

D3DCLIPSTATUS = Struct("D3DCLIPSTATUS", [
    (DWORD, "dwFlags"),
    (DWORD, "dwStatus"),
    (Float, "minx"),
    (Float, "maxx"),
    (Float, "miny"),
    (Float, "maxy"),
    (Float, "minz"),
    (Float, "maxz"),
])
LPD3DCLIPSTATUS = Pointer(D3DCLIPSTATUS)

D3DCLIPSTATUS = Flags(DWORD, [
    "D3DCLIPSTATUS_STATUS",
    "D3DCLIPSTATUS_EXTENTS2",
    "D3DCLIPSTATUS_EXTENTS3",
])

D3DSTATS = Struct("D3DSTATS", [
    (DWORD, "dwSize"),
    (DWORD, "dwTrianglesDrawn"),
    (DWORD, "dwLinesDrawn"),
    (DWORD, "dwPointsDrawn"),
    (DWORD, "dwSpansDrawn"),
    (DWORD, "dwVerticesProcessed"),
])
LPD3DSTATS = Pointer(D3DSTATS)

D3DEXECUTE = Flags(DWORD, [
    "D3DEXECUTE_CLIPPED",
    "D3DEXECUTE_UNCLIPPED",
])

D3DEXECUTEDATA = Struct("D3DEXECUTEDATA", [
    (DWORD, "dwSize"),
    (DWORD, "dwVertexOffset"),
    (DWORD, "dwVertexCount"),
    (DWORD, "dwInstructionOffset"),
    (DWORD, "dwInstructionLength"),
    (DWORD, "dwHVertexOffset"),
    (D3DSTATUS, "dsStatus"),
])
LPD3DEXECUTEDATA = Pointer(D3DEXECUTEDATA)

D3DPAL = Flags(DWORD, [
    "D3DPAL_FREE",
    "D3DPAL_READONLY",
    "D3DPAL_RESERVED",
])

D3DVERTEXBUFFERDESC = Struct("D3DVERTEXBUFFERDESC", [
    (DWORD, "dwSize"),
    (DWORD, "dwCaps"),
    (DWORD, "dwFVF"),
    (DWORD, "dwNumVertices"),
])
LPD3DVERTEXBUFFERDESC = Pointer(D3DVERTEXBUFFERDESC)

D3DVBCAPS = Flags(DWORD, [
    "D3DVBCAPS_SYSTEMMEMORY",
    "D3DVBCAPS_WRITEONLY",
    "D3DVBCAPS_OPTIMIZED",
    "D3DVBCAPS_DONOTCLIP",
])

D3DVOP = Flags(DWORD, [
    "D3DVOP_LIGHT",
    "D3DVOP_TRANSFORM",
    "D3DVOP_CLIP",
    "D3DVOP_EXTENTS",
])

D3DPV = Flags(DWORD, [
    "D3DPV_DONOTCOPYDATA",
])

D3DFVF = Flags(DWORD, [
    "D3DFVF_RESERVED0",
    "D3DFVF_XYZ",
    "D3DFVF_XYZRHW",
    "D3DFVF_XYZB1",
    "D3DFVF_XYZB2",
    "D3DFVF_XYZB3",
    "D3DFVF_XYZB4",
    "D3DFVF_XYZB5",
    "D3DFVF_NORMAL",
    "D3DFVF_RESERVED1",
    "D3DFVF_DIFFUSE",
    "D3DFVF_SPECULAR",
    #"D3DFVF_TEX0",
    #"D3DFVF_TEX1",
    #"D3DFVF_TEX2",
    #"D3DFVF_TEX3",
    #"D3DFVF_TEX4",
    #"D3DFVF_TEX5",
    #"D3DFVF_TEX6",
    #"D3DFVF_TEX7",
    #"D3DFVF_TEX8",
    "D3DFVF_RESERVED2",
    #"D3DFVF_TEXCOORDSIZE1(0)",
    #"D3DFVF_TEXCOORDSIZE2(0)",
    #"D3DFVF_TEXCOORDSIZE3(0)",
    #"D3DFVF_TEXCOORDSIZE4(0)",
    #"D3DFVF_TEXCOORDSIZE1(1)",
    #"D3DFVF_TEXCOORDSIZE2(1)",
    #"D3DFVF_TEXCOORDSIZE3(1)",
    #"D3DFVF_TEXCOORDSIZE4(1)",
    #"D3DFVF_TEXCOORDSIZE1(2)",
    #"D3DFVF_TEXCOORDSIZE2(2)",
    #"D3DFVF_TEXCOORDSIZE3(2)",
    #"D3DFVF_TEXCOORDSIZE4(2)",
    #"D3DFVF_TEXCOORDSIZE1(3)",
    #"D3DFVF_TEXCOORDSIZE2(3)",
    #"D3DFVF_TEXCOORDSIZE3(3)",
    #"D3DFVF_TEXCOORDSIZE4(3)",
])

D3DDP_PTRSTRIDE = Struct("D3DDP_PTRSTRIDE", [
    (LPVOID, "lpvData"),
    (DWORD, "dwStride"),
])

D3DDRAWPRIMITIVESTRIDEDDATA = Struct("D3DDRAWPRIMITIVESTRIDEDDATA", [
    (D3DDP_PTRSTRIDE, "position"),
    (D3DDP_PTRSTRIDE, "normal"),
    (D3DDP_PTRSTRIDE, "diffuse"),
    (D3DDP_PTRSTRIDE, "specular"),
    (Array(D3DDP_PTRSTRIDE, "D3DDP_MAXTEXCOORD"), "textureCoords"),
])
LPD3DDRAWPRIMITIVESTRIDEDDATA = Pointer(D3DDRAWPRIMITIVESTRIDEDDATA)

D3DVIS = Flags(DWORD, [
    "D3DVIS_INSIDE_FRUSTUM",
    "D3DVIS_INTERSECT_FRUSTUM",
    "D3DVIS_OUTSIDE_FRUSTUM",
    "D3DVIS_INSIDE_LEFT",
    "D3DVIS_INTERSECT_LEFT",
    "D3DVIS_OUTSIDE_LEFT",
    "D3DVIS_INSIDE_RIGHT",
    "D3DVIS_INTERSECT_RIGHT",
    "D3DVIS_OUTSIDE_RIGHT",
    "D3DVIS_INSIDE_TOP",
    "D3DVIS_INTERSECT_TOP",
    "D3DVIS_OUTSIDE_TOP",
    "D3DVIS_INSIDE_BOTTOM",
    "D3DVIS_INTERSECT_BOTTOM",
    "D3DVIS_OUTSIDE_BOTTOM",
    "D3DVIS_INSIDE_NEAR",
    "D3DVIS_INTERSECT_NEAR",
    "D3DVIS_OUTSIDE_NEAR",
    "D3DVIS_INSIDE_FAR",
    "D3DVIS_INTERSECT_FAR",
    "D3DVIS_OUTSIDE_FAR",
    "D3DVIS_MASK_FRUSTUM",
    "D3DVIS_MASK_LEFT",
    "D3DVIS_MASK_RIGHT",
    "D3DVIS_MASK_TOP",
    "D3DVIS_MASK_BOTTOM",
    "D3DVIS_MASK_NEAR",
    "D3DVIS_MASK_FAR",
])

D3DDEVINFOID = Flags(DWORD, [
    "D3DDEVINFOID_TEXTUREMANAGER",
    "D3DDEVINFOID_D3DTEXTUREMANAGER",
    "D3DDEVINFOID_TEXTURING",
])

D3DSTATEBLOCKTYPE = Enum("D3DSTATEBLOCKTYPE", [
    "D3DSBT_ALL",
    "D3DSBT_PIXELSTATE",
    "D3DSBT_VERTEXSTATE",
])

D3DVERTEXBLENDFLAGS = Enum("D3DVERTEXBLENDFLAGS", [
    "D3DVBLEND_DISABLE",
    "D3DVBLEND_1WEIGHT",
    "D3DVBLEND_2WEIGHTS",
    "D3DVBLEND_3WEIGHTS",
])

D3DTEXTURETRANSFORMFLAGS = Enum("D3DTEXTURETRANSFORMFLAGS", [
    "D3DTTFF_DISABLE",
    "D3DTTFF_COUNT1",
    "D3DTTFF_COUNT2",
    "D3DTTFF_COUNT3",
    "D3DTTFF_COUNT4",
    "D3DTTFF_PROJECTED",
])

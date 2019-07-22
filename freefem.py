# -*- coding: utf-8 -*-
"""
    pygments.lexers.freefem
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexer for FreeFem++ language.

    :copyright: see README.md.
    :license: GPLv3, see LICENSE for details.
"""

import re

from pygments.lexer import RegexLexer, include, bygroups, inherit, words, \
    default
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation

from pygments.lexers.c_cpp import CLexer, CppLexer
from pygments.lexers import _mql_builtins

__all__ = ['FreeFemLexer']


class FreeFemLexer(CppLexer):
    """
    For `FreeFem++ <http://www.freefem.org/>`_ source.

    This is an extension of the CppLexer, as the FreeFem Language is a superset
    of C++
    """

    name = 'Freefem'
    aliases = ['freefem']
    filenames = ['*.edp']
    mimetypes = ['text/x-freefem']

    # Language operators
    operators = set(('+', '-', '*', '.*', '/', './', '%', '^', '^-1', ':', '\'', '#'))

    # types
    types = set((
    	'bool',
		'border',
		'complex',
		'dmatrix',
		'fespace',
		'func',
		'gslspline',
		'ifstream',
		'int',
		'macro',
		'matrix',
		'mesh',
		'mesh3',
        'meshS',
		'mpiComm',
		'mpiGroup',
		'mpiRequest',
		'NewMacro',
		'EndMacro',
		'ofstream',
		'Pmmap',
		'problem',
		'Psemaphore',
		'real',
		'solve',
		'string',
		'varf'
    ))
    
    # finite element spaces
    fespaces = set((
		'BDM1',
		'BDM1Ortho',
		'Edge03d',
		'Edge13d',
		'Edge23d',
		'FEQF',
		'HCT',
		'P0',
		'P03d',
		'P0Edge',
		'P1',
		'P13d',
		'P1b',
		'P1b3d',
		'P1bl',
		'P1bl3d',
		'P1dc',
		'P1Edge',
		'P1nc',
		'P2',
		'P23d',
		'P2b',
		'P2BR',
		'P2dc',
		'P2Edge',
		'P2h',
		'P2Morley',
		'P2pnc',
		'P3',
		'P3dc',
		'P3Edge',
		'P4',
		'P4dc',
		'P4Edge',
		'P5Edge',
		'RT0',
		'RT03d',
		'RT0Ortho',
		'RT1',
		'RT1Ortho',
		'RT2',
		'RT2Ortho'
    ))
    
    # preprocessor
    preprocessor = set((
		'ENDIFMACRO',
		'include',
		'IFMACRO',
		'load'
    ))
    
    # Language keywords
    keywords = set((
		'adj',
		'append',
		'area',
		'ARGV',
		'be',
		'binary',
		'BoundaryEdge',
		'bordermeasure',
		'CG',
		'Cholesky',
		'cin',
		'cout',
		'Crout',
		'default',
		'diag',
		'edgeOrientation',
		'endl',
		'false',
		'ffind',
		'FILE',
		'find',
		'fixed',
		'flush',
		'GMRES',
		'good',
		'hTriangle',
		'im',
		'imax',
		'imin',
		'InternalEdge',
		'l1',
		'l2',
		'label',
		'lenEdge',
		'length',
		'LINE',
		'linfty',
		'LU',
		'm',
		'max',
		'measure',
		'min',
		'mpiAnySource',
		'mpiBAND',
		'mpiBXOR',
		'mpiCommWorld',
		'mpiLAND',
		'mpiLOR',
		'mpiLXOR',
		'mpiMAX',
		'mpiMIN',
		'mpiPROD',
		'mpirank',
		'mpisize',
		'mpiSUM',
		'mpiUndefined',
		'n',
		'N',
		'nbe',
		'ndof',
		'ndofK',
		'noshowbase',
		'noshowpos',
		'notaregion',
		'nt',
		'nTonEdge',
		'nuEdge',
		'nuTriangle',
		'nv',
        'nbnomanifold',
		'P',
		'pi',
		'precision',
		'qf1pE',
		'qf1pElump',
		'qf1pT',
		'qf1pTlump',
		'qfV1',
		'qfV1lump',
		'qf2pE',
		'qf2pT',
		'qf2pT4P1',
		'qfV2',
		'qf3pE',
		'qf4pE',
		'qf5pE',
		'qf5pT',
		'qfV5',
		'qf7pT',
		'qf9pT',
		'qfnbpE',
		'quantile',
		're',
		'region',
		'rfind',
		'scientific',
		'searchMethod',
		'setw',
		'showbase',
		'showpos',
		'sparsesolver',
		'sum',
		'tellp',
		'true',
		'UMFPACK',
		'unused',
		'whoinElement',
		'verbosity',
		'version',
		'volume',
		'x',
		'y',
		'z'
    ))
    
    # Language shipped functions and class ( )
    functions = set((
		'abs',
		'acos',
		'acosh',
		'adaptmesh',
		'adj',
		'AffineCG',
		'AffineGMRES',
		'arg',
		'asin',
		'asinh',
		'assert',
		'atan',
		'atan2',
		'atanh',
		'atof',
		'atoi',
		'BFGS',
		'broadcast',
		'buildlayers',
		'buildmesh',
        'buildSurface',
		'ceil',
		'chi',
		'complexEigenValue',
		'copysign',
		'change',
		'checkmovemesh',
		'clock',
		'cmaes',
		'conj',
		'convect',
		'cos',
		'cosh',
		'cube',
		'd',
		'dd',
		'dfft',
		'diffnp',
		'diffpos',
		'dimKrylov',
		'dist',
		'dumptable',
		'dx',
		'dxx',
		'dxy',
		'dxz',
		'dy',
		'dyx',
		'dyy',
		'dyz',
		'dz',
		'dzx',
		'dzy',
		'dzz',
		'EigenValue',
		'emptymesh',
		'erf',
		'erfc',
		'exec',
		'exit',
		'exp',
        'extract',
		'fdim',
		'floor',
		'fmax',
		'fmin',
		'fmod',
		'freeyams',
        'Gamma',
		'getARGV',
		'getline',
		'gmshload',
		'gmshload3',
		'gslcdfugaussianP',
		'gslcdfugaussianQ',
		'gslcdfugaussianPinv',
		'gslcdfugaussianQinv',
		'gslcdfgaussianP',
		'gslcdfgaussianQ',
		'gslcdfgaussianPinv',
		'gslcdfgaussianQinv',
		'gslcdfgammaP',
		'gslcdfgammaQ',
		'gslcdfgammaPinv',
		'gslcdfgammaQinv',
		'gslcdfcauchyP',
		'gslcdfcauchyQ',
		'gslcdfcauchyPinv',
		'gslcdfcauchyQinv',
		'gslcdflaplaceP',
		'gslcdflaplaceQ',
		'gslcdflaplacePinv',
		'gslcdflaplaceQinv',
		'gslcdfrayleighP',
		'gslcdfrayleighQ',
		'gslcdfrayleighPinv',
		'gslcdfrayleighQinv',
		'gslcdfchisqP',
		'gslcdfchisqQ',
		'gslcdfchisqPinv',
		'gslcdfchisqQinv',
		'gslcdfexponentialP',
		'gslcdfexponentialQ',
		'gslcdfexponentialPinv',
		'gslcdfexponentialQinv',
		'gslcdfexppowP',
		'gslcdfexppowQ',
		'gslcdftdistP',
		'gslcdftdistQ',
		'gslcdftdistPinv',
		'gslcdftdistQinv',
		'gslcdffdistP',
		'gslcdffdistQ',
		'gslcdffdistPinv',
		'gslcdffdistQinv',
		'gslcdfbetaP',
		'gslcdfbetaQ',
		'gslcdfbetaPinv',
		'gslcdfbetaQinv',
		'gslcdfflatP',
		'gslcdfflatQ',
		'gslcdfflatPinv',
		'gslcdfflatQinv',
		'gslcdflognormalP',
		'gslcdflognormalQ',
		'gslcdflognormalPinv',
		'gslcdflognormalQinv',
		'gslcdfgumbel1P',
		'gslcdfgumbel1Q',
		'gslcdfgumbel1Pinv',
		'gslcdfgumbel1Qinv',
		'gslcdfgumbel2P',
		'gslcdfgumbel2Q',
		'gslcdfgumbel2Pinv',
		'gslcdfgumbel2Qinv',
		'gslcdfweibullP',
		'gslcdfweibullQ',
		'gslcdfweibullPinv',
		'gslcdfweibullQinv',
		'gslcdfparetoP',
		'gslcdfparetoQ',
		'gslcdfparetoPinv',
		'gslcdfparetoQinv',
		'gslcdflogisticP',
		'gslcdflogisticQ',
		'gslcdflogisticPinv',
		'gslcdflogisticQinv',
		'gslcdfbinomialP',
		'gslcdfbinomialQ',
		'gslcdfpoissonP',
		'gslcdfpoissonQ',
		'gslcdfgeometricP',
		'gslcdfgeometricQ',
		'gslcdfnegativebinomialP',
		'gslcdfnegativebinomialQ',
		'gslcdfpascalP',
		'gslcdfpascalQ',
		'gslinterpakima',
		'gslinterpakimaperiodic',
		'gslinterpcsplineperiodic',
		'gslinterpcspline',
		'gslinterpsteffen',
		'gslinterplinear',
		'gslinterppolynomial',
		'gslranbernoullipdf',
		'gslranbeta',
		'gslranbetapdf',
		'gslranbinomialpdf',
		'gslranexponential',
		'gslranexponentialpdf',
		'gslranexppow',
		'gslranexppowpdf',
		'gslrancauchy',
		'gslrancauchypdf',
		'gslranchisq',
		'gslranchisqpdf',
		'gslranerlang',
		'gslranerlangpdf',
		'gslranfdist',
		'gslranfdistpdf',
		'gslranflat',
		'gslranflatpdf',
		'gslrangamma',
		'gslrangammaint',
		'gslrangammapdf',
		'gslrangammamt',
		'gslrangammaknuth',
		'gslrangaussian',
		'gslrangaussianratiomethod',
		'gslrangaussianziggurat',
		'gslrangaussianpdf',
		'gslranugaussian',
		'gslranugaussianratiomethod',
		'gslranugaussianpdf',
		'gslrangaussiantail',
		'gslrangaussiantailpdf',
		'gslranugaussiantail',
		'gslranugaussiantailpdf',
		'gslranlandau',
		'gslranlandaupdf',
		'gslrangeometricpdf',
		'gslrangumbel1',
		'gslrangumbel1pdf',
		'gslrangumbel2',
		'gslrangumbel2pdf',
		'gslranlogistic',
		'gslranlogisticpdf',
		'gslranlognormal',
		'gslranlognormalpdf',
		'gslranlogarithmicpdf',
		'gslrannegativebinomialpdf',
		'gslranpascalpdf',
		'gslranpareto',
		'gslranparetopdf',
		'gslranpoissonpdf',
		'gslranrayleigh',
		'gslranrayleighpdf',
		'gslranrayleightail',
		'gslranrayleightailpdf',
		'gslrantdist',
		'gslrantdistpdf',
		'gslranlaplace',
		'gslranlaplacepdf',
		'gslranlevy',
		'gslranweibull',
		'gslranweibullpdf',
		'gslsfairyAi',
		'gslsfairyBi',
		'gslsfairyAiscaled',
		'gslsfairyBiscaled',
		'gslsfairyAideriv',
		'gslsfairyBideriv',
		'gslsfairyAiderivscaled',
		'gslsfairyBiderivscaled',
		'gslsfairyzeroAi',
		'gslsfairyzeroBi',
		'gslsfairyzeroAideriv',
		'gslsfairyzeroBideriv',
		'gslsfbesselJ0',
		'gslsfbesselJ1',
		'gslsfbesselJn',
		'gslsfbesselY0',
		'gslsfbesselY1',
		'gslsfbesselYn',
		'gslsfbesselI0',
		'gslsfbesselI1',
		'gslsfbesselIn',
		'gslsfbesselI0scaled',
		'gslsfbesselI1scaled',
		'gslsfbesselInscaled',
		'gslsfbesselK0',
		'gslsfbesselK1',
		'gslsfbesselKn',
		'gslsfbesselK0scaled',
		'gslsfbesselK1scaled',
		'gslsfbesselKnscaled',
		'gslsfbesselj0',
		'gslsfbesselj1',
		'gslsfbesselj2',
		'gslsfbesseljl',
		'gslsfbessely0',
		'gslsfbessely1',
		'gslsfbessely2',
		'gslsfbesselyl',
		'gslsfbesseli0scaled',
		'gslsfbesseli1scaled',
		'gslsfbesseli2scaled',
		'gslsfbesselilscaled',
		'gslsfbesselk0scaled',
		'gslsfbesselk1scaled',
		'gslsfbesselk2scaled',
		'gslsfbesselklscaled',
		'gslsfbesselJnu',
		'gslsfbesselYnu',
		'gslsfbesselInuscaled',
		'gslsfbesselInu',
		'gslsfbesselKnuscaled',
		'gslsfbesselKnu',
		'gslsfbessellnKnu',
		'gslsfbesselzeroJ0',
		'gslsfbesselzeroJ1',
		'gslsfbesselzeroJnu',
		'gslsfclausen',
		'gslsfhydrogenicR1',
		'gslsfdawson',
		'gslsfdebye1',
		'gslsfdebye2',
		'gslsfdebye3',
		'gslsfdebye4',
		'gslsfdebye5',
		'gslsfdebye6',
		'gslsfdilog',
		'gslsfmultiply',
		'gslsfellintKcomp',
		'gslsfellintEcomp',
		'gslsfellintPcomp',
		'gslsfellintDcomp',
		'gslsfellintF',
		'gslsfellintE',
		'gslsfellintRC',
		'gslsferfc',
		'gslsflogerfc',
		'gslsferf',
		'gslsferfZ',
		'gslsferfQ',
		'gslsfhazard',
		'gslsfexp',
		'gslsfexpmult',
		'gslsfexpm1',
		'gslsfexprel',
		'gslsfexprel2',
		'gslsfexpreln',
		'gslsfexpintE1',
		'gslsfexpintE2',
		'gslsfexpintEn',
		'gslsfexpintE1scaled',
		'gslsfexpintE2scaled',
		'gslsfexpintEnscaled',
		'gslsfexpintEi',
		'gslsfexpintEiscaled',
		'gslsfShi',
		'gslsfChi',
		'gslsfexpint3',
		'gslsfSi',
		'gslsfCi',
		'gslsfatanint',
		'gslsffermidiracm1',
		'gslsffermidirac0',
		'gslsffermidirac1',
		'gslsffermidirac2',
		'gslsffermidiracint',
		'gslsffermidiracmhalf',
		'gslsffermidirachalf',
		'gslsffermidirac3half',
		'gslsffermidiracinc0',
		'gslsflngamma',
		'gslsfgamma',
		'gslsfgammastar',
		'gslsfgammainv',
		'gslsftaylorcoeff',
		'gslsffact',
		'gslsfdoublefact',
		'gslsflnfact',
		'gslsflndoublefact',
		'gslsflnchoose',
		'gslsfchoose',
		'gslsflnpoch',
		'gslsfpoch',
		'gslsfpochrel',
		'gslsfgammaincQ',
		'gslsfgammaincP',
		'gslsfgammainc',
		'gslsflnbeta',
		'gslsfbeta',
		'gslsfbetainc',
		'gslsfgegenpoly1',
		'gslsfgegenpoly2',
		'gslsfgegenpoly3',
		'gslsfgegenpolyn',
		'gslsfhyperg0F1',
		'gslsfhyperg1F1int',
		'gslsfhyperg1F1',
		'gslsfhypergUint',
		'gslsfhypergU',
		'gslsfhyperg2F0',
		'gslsflaguerre1',
		'gslsflaguerre2',
		'gslsflaguerre3',
		'gslsflaguerren',
		'gslsflambertW0',
		'gslsflambertWm1',
		'gslsflegendrePl',
		'gslsflegendreP1',
		'gslsflegendreP2',
		'gslsflegendreP3',
		'gslsflegendreQ0',
		'gslsflegendreQ1',
		'gslsflegendreQl',
		'gslsflegendrePlm',
		'gslsflegendresphPlm',
		'gslsflegendrearraysize',
		'gslsfconicalPhalf',
		'gslsfconicalPmhalf',
		'gslsfconicalP0',
		'gslsfconicalP1',
		'gslsfconicalPsphreg',
		'gslsfconicalPcylreg',
		'gslsflegendreH3d0',
		'gslsflegendreH3d1',
		'gslsflegendreH3d',
		'gslsflog',
		'gslsflogabs',
		'gslsflog1plusx',
		'gslsflog1plusxmx',
		'gslsfpowint',
		'gslsfpsiint',
		'gslsfpsi',
		'gslsfpsi1piy',
		'gslsfpsi1int',
		'gslsfpsi1',
		'gslsfpsin',
		'gslsfsynchrotron1',
		'gslsfsynchrotron2',
		'gslsftransport2',
		'gslsftransport3',
		'gslsftransport4',
		'gslsftransport5',
		'gslsfsin',
		'gslsfcos',
		'gslsfhypot',
		'gslsfsinc',
		'gslsflnsinh',
		'gslsflncosh',
		'gslsfanglerestrictsymm',
		'gslsfanglerestrictpos',
		'gslsfzetaint',
		'gslsfzeta',
		'gslsfzetam1',
		'gslsfzetam1int',
		'gslsfhzeta',
		'gslsfetaint',
		'gslsfeta',
		'imag',
		'int1d',
		'int2d',
		'int3d',
		'intalledges',
		'intallfaces',
		'interpolate',
		'invdiff',
		'invdiffnp',
		'invdiffpos',
		'Isend',
		'isInf',
		'isNaN',
		'isoline',
		'Irecv',
		'j0',
		'j1',
		'jn',
		'jump',
		'lgamma',
		'LinearCG',
		'LinearGMRES',
		'log',
		'log10',
		'lrint',
		'lround',
		'max',
		'mean',
		'medit',
		'min',
		'mmg3d',
		'movemesh',
		'movemesh23',
        'movemesh3'
        'movemeshS'
		'mpiAlltoall',
		'mpiAlltoallv',
		'mpiAllgather',
		'mpiAllgatherv',
		'mpiAllReduce',
		'mpiBarrier',
		'mpiGather',
		'mpiGatherv',
		'mpiRank',
		'mpiReduce',
		'mpiScatter',
		'mpiScatterv',
		'mpiSize',
		'mpiWait',
		'mpiWaitAny',
		'mpiWtick',
		'mpiWtime',
		'mshmet',
		'NaN',
		'NLCG',
		'on',
		'plot',
		'polar',
		'Post',
		'pow',
		'processor',
		'processorblock',
		'projection',
		'randinit',
		'randint31',
		'randint32',
		'random',
		'randreal1',
		'randreal2',
		'randreal3',
		'randres53',
		'Read',
		'readmesh',
		'readmesh3',
		'Recv',
		'rint',
		'round',
		'savemesh',
		'savesol',
		'savevtk',
		'seekg',
		'Sent',
		'set',
		'sign',
		'signbit',
		'sin',
		'sinh',
		'sort',
		'splitComm',
		'splitmesh',
		'sqrt',
		'square',
        'square3',
		'srandom',
		'srandomdev',
		'Stringification',
		'swap',
		'system',
		'tan',
		'tanh',
		'tellg',
		'tetg',
		'tetgconvexhull',
		'tetgreconstruction',
		'tetgtransfo',
		'tgamma',
		'triangulate',
		'trunc',
		'Wait',
		'Write',
		'y0',
		'y1',
		'yn'
    ))
    
    # function parameters
    parameters = set((
		'A',
		'A1',
		'abserror',
		'absolute',
		'aniso',
		'aspectratio',
		'B',
		'B1',
		'bb',
		'beginend',
		'bin',
		'boundary',
		'bw',
		'close',
		'cmm',
		'coef',
		'composante',
		'cutoff',
		'datafilename',
		'dataname',
		'dim',
		'distmax',
		'displacement',
		'doptions',
		'dparams',
		'eps',
		'err',
		'errg',
		'facemerge',
		'facetcl',
		'factorize',
		'file',
		'fill',
		'fixedborder',
		'flabel',
		'flags',
		'floatmesh',
		'floatsol',
		'fregion',
		'gradation',
		'grey',
		'hmax',
		'hmin',
		'holelist',
		'hsv',
		'init',
		'inquire',
		'inside',
		'IsMetric',
		'iso',
		'ivalue',
		'keepbackvertices',
		'label',
		'labeldown',
		'labelmid',
		'labelup',
		'levelset',
		'loptions',
		'lparams',
		'maxit',
		'maxsubdiv',
		'meditff',
		'mem',
		'memory',
		'metric',
		'mode',
		'nbarrow',
		'nbiso',
		'nbiter',
		'nbjacoby',
		'nboffacetcl',
		'nbofholes',
		'nbofregions',
		'nbregul',
		'nbsmooth',
		'nbvx',
		'ncv',
		'nev',
		'nomeshgeneration',
		'normalization',
		'omega',
		'op',
		'optimize',
		'option',
		'options',
		'order',
		'orientation',
		'periodic',
		'power',
		'precon',
		'prev',
		'ps',
		'ptmerge',
		'qfe',
		'qforder',
		'qft',
		'qfV',
		'ratio',
		'rawvector',
        'refe',
		'reffacelow',
		'reffacemid',
		'reffaceup',
		'refnum',
        'reft',
		'reftet',
		'reftri',
		'region',
		'regionlist',
		'renumv',
        'renumt',
		'rescaling',
		'ridgeangle',
        'rmledges',
        'rmInternalEdges',
		'save',
		'sigma',
		'sizeofvolume',
		'smoothing',
		'solver',
		'sparams',
		'split',
		'splitin2',
		'splitpbedge',
		'stop',
		'strategy',
		'swap',
		'switch',
		'sym',
		't',
		'tgv',
		'thetamax',
		'tol',
		'tolpivot',
		'tolpivotsym',
		'transfo',
		'U2Vc',
		'value',
		'varrow',
		'vector',
		'veps',
		'viso',
		'wait',
		'width',
		'withsurfacemesh',
		'WindowIndex',
		'which',
		'zbound'
    ))

    # deprecated
    deprecated = set((
		'fixeborder'
    ))

    # do not highlight
    suppress_highlight = set((
		'alignof',
		'asm',
		'constexpr',
		'decltype',
		'div',
		'double',
		'grad',
		'mutable',
		'namespace',
		'noexcept',
		'restrict',
		'static_assert',
		'template',
		'this',
		'thread_local',
		'typeid',
		'typename',
		'using'
    ))

    def get_tokens_unprocessed(self, text):
        for index, token, value in CppLexer.get_tokens_unprocessed(self, text):
            if value in self.operators:
                yield index, Operator, value
            elif value in self.types:
                yield index, Keyword.Type, value
            elif value in self.fespaces:
                yield index, Name.Class, value
            elif value in self.preprocessor:
                yield index, Comment.Preproc, value
            elif value in self.keywords:
                yield index, Keyword.Reserved, value
            elif value in self.functions:
                yield index, Name.Function, value
            elif value in self.parameters:
                yield index, Keyword.Pseudo, value
            elif value in self.suppress_highlight:
                yield index, Name, value
            else:
                yield index, token, value

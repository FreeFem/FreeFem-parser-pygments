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
    operators = set(('+', '-', '*', '/', '^', ':', '\''))

    # types
    types = set((
		'border',
		'complex',
		'dmatrix',
		'fespace',
		'func',
		'ifstream',
		'macro',
		'matrix',
		'mesh',
		'mesh3',
		'ofstream',
		'problem',
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
    	'Edge13D',
    	'Edge23D',
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
    	'P1bl3d'
    	'P1dc',
    	'P1Edge',
    	'P1nc',
    	'P2',
    	'P23d',
    	'P2b',
    	'P2BR',
    	'P2dc',
    	'P2Edge',
    	'P2Morley',
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
    	'RT1Ortho'
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
    	'be',
    	'binary',
    	'bordermeasure',
    	'CG',
    	'Cholesky',
    	'cin',
    	'cout',
    	'Crout',
    	'diag',
    	'endl',
    	'flush',
    	'GMRES',
    	'hTriangle',
    	'label',
    	'lenEdge',
    	'LU',
    	'm',
    	'measure',
    	'n',
    	'N',
    	'nbe',
    	'nt',
    	'nuTriangle',
    	'nv',
    	'P',
    	'pi',
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
    	'qf5pE',
    	'qf5pT',
    	'qfV5',
    	'qf7pT',
    	'qf9pT',
    	'region',
    	'sparsesolver',
    	'whoinElement',
    	'verbosity',
    	'version',
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
    	'asin',
    	'asinh',
    	'assert',
    	'atan',
    	'atan2',
    	'atanh',
    	'BFGS',
    	'buildlayers',
    	'buildmesh',
    	'ceil',
    	'change',
    	'checkmovemesh',
    	'clock',
    	'cmaes',
    	'conj',
    	'convect',
    	'cos',
    	'cosh',
    	'cube',
    	'dfft',
    	'diffnp',
    	'diffpos',
    	'dist',
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
    	'fdim',
    	'floor',
    	'fmax',
    	'fmin',
    	'fmod',
    	'freeyams',
    	'getline',
    	'imag',
    	'int1d',
    	'int2d',
    	'int3d',
    	'intalledges',
    	'interpolate',
    	'invdiffnp',
    	'invdiffpos',
    	'isoline',
    	'j0',
    	'j1',
    	'jn',
    	'jump',
    	'LinearCG',
    	'LinearGMRES',
    	'log',
    	'log10',
    	'max',
    	'mean',
    	'medit',
    	'min',
    	'mmg3d',
    	'movemesh',
    	'movemesh23',
    	'mshmet',
    	'NLCG',
    	'on',
    	'plot',
    	'polar',
    	'pow',
    	'projection',
    	'readmesh',
    	'readmesh3',
    	'round',
    	'savemesh',
    	'savesol',
    	'set',
    	'seekg',
    	'sin',
    	'sinh',
    	'sort',
    	'splitmesh',
    	'sqrt',
    	'square',
    	'system',
    	'tan',
    	'tanh',
    	'tellg',
    	'tetg',
    	'tetgconvexhull',
    	'tetgreconstruction',
    	'tetgtransfo',
    	'triangulate',
    	'trunc',
    	'y0',
    	'y1',
    	'yn'
    ))
    
    # function parameters
    parameters = set((
    	'abserror',
    	'absolute',
    	'aniso',
    	'aspectratio',
    	'bb',
    	'beginend',
    	'boundary',
    	'bw',
    	'close',
    	'cmm',
    	'coef',
    	'cutoff',
    	'datafilename',
    	'dataname',
    	'dim',
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
    	'keepbackvertices',
    	'label',
    	'labeldown',
    	'labelmid',
    	'labelup',
    	'levelset',
    	'loptions',
    	'lparams',
    	'maxsubdiv',
    	'mem',
    	'memory',
    	'metric',
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
    	'nomeshgeneration',
    	'normalization',
    	'omega',
    	'op',
    	'option',
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
    	'ratio',
    	'reftet',
    	'region',
    	'regionlist',
    	'rescaling',
    	'ridgeangle',
    	'sizeofvolume',
    	'smoothing',
    	'solver',
    	'sparams',
    	'split',
    	'splitin2',
    	'splitpbedge',
    	'stop',
    	'strategy',
    	't',
    	'tgv',
    	'thetamax',
    	'tolpivot',
    	'tolpivotsym',
    	'transfo',
    	'U2Vc',
    	'value',
    	'varrow',
    	'veps',
    	'viso',
    	'wait',
    	'width',
    	'WindowIndex',
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

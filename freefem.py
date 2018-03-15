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
    'mesh', 'macro', 'problem', 'solve', 'fespace', 'varf', 'matrix', 'dmatrix', 'real', 'func', 'complex', 'mesh3', 'string', 'border', 
    'ofstream', 'ifstream'
    ))
    
    # finite element spaces
    fespaces = set((
    'P0', 'P03d', 'P0Edge', 'P1', 'P13d', 'P1dc', 'P1b', 'P1b3d', 'P1bl', 'P1bl3d', 'P1nc', 'P2', 'P23d', 'P2b', 'P2dc', 'RT0', 'RT03d', 'RT0Ortho', 'Edge03d', 'P3', 'P3dc', 'P4', 'P4dc', 'P1Edge', 'P2Edge', 'P3Edge', 'P4Edge', 'P5Edge', 'P2Morley', 'HCT', 'P2BR', 'RT1', 'RT1Ortho', 'BDM1', 'BDM1Ortho', 'Edge13D', 'Edge23D', 'FEQF'
    ))
    
    # preprocessor
    preprocessor = set((
    'include', 'load'
    ))
    
    # Language keywords
    keywords = set((
    'CG', 'Cholesky', 'Crout', 'GMRES',  'LU', 'N', 'P', 'pi',
    'sparsesolver','verbosity', 'version', 'x', 'y', 'z', 
    'qf1pE', 'qf2pE', 'qf3pE', 'qf5pE', 'qf1pElump', 'qf1pT', 'qf2pT', 'qf5pT', 'qf1pTlump', 'qf2pT4P1', 'qf7pT', 'qf9pT', 'qfV1', 'qfV2', 'qfV5', 'qfV1lump', 
    'append', 'binary', 'flush', 'label', 'region'
    ))
    
    # Language shipped functions and class ( )
    functions = set((
    'acos', 'acosh', 'adaptmesh', 'adj', 'AffineCG', 'AffineGMRES', 'asin',
    'asinh', 'assert', 'atan', 'atan2', 'atanh', 'BFGS', 'buildlayers', 'buildmesh', 'getline', 'seekg', 'tellg', 
    'ceil', 'change', 'checkmovemesh', 'clock', 'cmaes', 'conj', 'convect', 'cos',
    'cosh', 'cube', 'dfft', 'diffnp', 'diffpos', 'dist', 'dx', 'dxx', 'dxy', 'dxz', 'dy', 'dyx', 'dyy', 'dyz', 'dz', 'dzx', 'dzy', 'dzz',
    'EigenValue', 'emptymesh', 'erf', 'erfc', 'exec', 'exit', 'exp', 'fdim', 'floor', 'fmax', 'fmin', 'fmod',
    'imag', 'int1d', 'int2d', 'int3d', 'intalledges', 'interpolate', 'invdiffnp',
    'invdiffpos', 'isoline', 'j0', 'j1', 'jn', 'jump', 'LinearCG', 'LinearGMRES',
    'log', 'log10', 'max', 'mean', 'medit', 'min', 'movemesh', 'movemesh23', 'NLCG',
    'on', 'plot', 'polar', 'pow', 'projection', 'readmesh', 'readmesh3', 'round',
    'savemesh', 'savesol', 'set', 'sin', 'sinh', 'sort', 'splitmesh', 'square', 'tan',
    'tanh', 'tetg', 'tetgconvexhull', 'tetgreconstruction', 'tetgtransfo', 'trunc',
    'y0', 'y1', 'yn', 'sqrt'))
    
    # function parameters
    parameters = set((
    'hmin', 'hmax', 'err', 'errg', 'nbvx', 'nbsmooth', 'nbjacoby', 'ratio', 'omega', 'iso', 'abserror', 'cutoff', 'inquire', 'splitpbedge', 'maxsubdiv', 'keepbackvertices',
    'isMetric', 'power', 'thetamax', 'splitin2', 'metric', 'nomeshgeneration', 'rescaling', 'periodic', 'cmm', 'flags', 'qfe', 'qforder', 'fixedborder', 'precon',
    'nbiter', 'eps', 'veps', 'stop','label', 'region', 'flabel', 'fregion', 'inside', 't', 'op', 'U2Vc', 'facemerge', 'ptmerge', 'orientation', 'wait', 'ps', 'coef',
    'fill', 'value', 'aspectratio', 'bb', 'nbiso', 'nbarrow', 'viso', 'varrow', 'bw', 'grey', 'hsv', 'boundary', 'dim', 'prev', 'WindowIndex', 'split'
    ))

    # deprecated
    deprecated = set((
    'fixeborder'
    ))
	
    # do not highlight
    suppress_highlight = set((
    'namespace', 'template', 'mutable', 'using', 'asm', 'typeid', 
    'typename', 'this', 'alignof', 'constexpr', 'decltype', 'noexcept', 
    'static_assert', 'thread_local', 'restrict', 'grad', 'div', 'double'
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

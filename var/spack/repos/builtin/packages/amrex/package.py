##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


# class Amrex(CMakePackage):
class Amrex(AutotoolsPackage):
    """AMReX is a publicly available software framework designed
    for building massively parallel block- structured adaptive
    mesh refinement (AMR) applications."""

    homepage = "https://amrex-codes.github.io/amrex/"
    git      = "https://github.com/AMReX-Codes/amrex.git"

    version('18.08.1', tag='18.08.1')
    version('18.07', tag='18.07')
    version('18.06', tag='18.06')
    version('18.05', tag='18.05')

    version('develop', branch='development')
    version('master', branch='master')

    # Config options
    variant('dimensions', default='3',
            description='Dimensionality', values=('2', '3'))
    # variant('shared',  default=False,
    #         description='Build shared library')
    variant('mpi',          default=True,
            description='Build with MPI support')
    variant('openmp',       default=False,
            description='Build with OpenMP support')
    # variant('precision',  default='double',
    #         description='Real precision (double/single)',
    #         values=('single', 'double'))
    # variant('eb',  default=False,
    #         description='Build Embedded Boundary classes')
    variant('fortran',  default=False,
            description='Build Fortran API')
    variant('linear_solvers', default=True,
            description='Build linear solvers')
    # variant('amrdata',    default=False,
    #         description='Build data services')
    variant('particles',  default=False,
            description='Build particle classes')
    # variant('build_type', default='Release',
    #         description='The build type to build',
    #         values=('Debug', 'Release'))

    # Build dependencies
    depends_on('mpi', when='+mpi')
    # depends_on('python@2.7:', type='build')
    # depends_on('cmake@3.5:',  type='build')
    conflicts('%clang')

    def _yes_no(self, option):
        return 'yes' if option in self.spec else 'no'

    def configure_args(self):
        return [
            '--dim', str(self.spec.variants['dimensions'].value),
            '--with-mpi', self._yes_no('+mpi'),
            '--with-omp', self._yes_no('+openmp'),
            '--debug', 'no',
            # '--debug', 'yes' if self.spec['build_type'] == 'Debug' else 'no',
            '--enable-particle', self._yes_no('+particles'),
            '--enable-fortran-api', self._yes_no('+fortran'),
            '--enable-linear-solver', self._yes_no('+linear_solvers'),
            '--enable-xsdk-defaults', 'yes']

    # def cmake_is_on(self, option):
    #     return 'ON' if option in self.spec else 'OFF'

    # def cmake_args(self):
    #     args = [
    #         '-DUSE_XSDK_DEFAULTS=ON',
    #         '-DDIM:STRING=%s' % self.spec.variants['dimensions'].value,
    #         '-DBUILD_SHARED_LIBS:BOOL=%s' % self.cmake_is_on('+shared'),
    #         '-DENABLE_MPI:BOOL=%s' % self.cmake_is_on('+mpi'),
    #         '-DENABLE_OMP:BOOL=%s' % self.cmake_is_on('+openmp'),
    #         '-DXSDK_PRECISION:STRING=%s' %
    #         self.spec.variants['precision'].value.upper(),
    #         '-DENABLE_EB:BOOL=%s' % self.cmake_is_on('+eb'),
    #         '-DXSDK_ENABLE_Fortran:BOOL=%s' % self.cmake_is_on('+fortran'),
    #         '-DENABLE_LINEAR_SOLVERS:BOOL=%s' %
    #         self.cmake_is_on('+linear_solvers'),
    #         '-DENABLE_AMRDATA:BOOL=%s' % self.cmake_is_on('+amrdata'),
    #         '-DENABLE_PARTICLES:BOOL=%s' % self.cmake_is_on('+particles')
    #     ]
    #     return args

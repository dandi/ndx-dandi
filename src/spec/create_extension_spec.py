# -*- coding: utf-8 -*-

import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec, NWBDatasetSpec
# TODO: import the following spec classes as needed
# from pynwb.spec import NWBDatasetSpec, NWBLinkSpec, NWBDtypeSpec, NWBRefSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc="""DANDI project extension""",
        name="""ndx-dandi""",
        version="""0.1.0""",
        author=list(map(str.strip, """Yaroslav O Halchenko""".split(','))),
        contact=list(map(str.strip, """debian@onerussian.com""".split(',')))
    )

    # TODO: specify the neurodata_types that are used by the extension as well
    # as in which namespace they are found
    # this is similar to specifying the Python modules that need to be imported
    # to use your new data types
    ns_builder.include_type('Subject', namespace='core')

    # TODO: define your new data types
    # see https://pynwb.readthedocs.io/en/latest/extensions.html#extending-nwb
    # for more information
    dandi_subject = NWBGroupSpec(
        neurodata_type_def='DANDISubject',
        neurodata_type_inc='Subject',
        doc="TODO: somehow inherit",
        datasets=[NWBDatasetSpec(
         name='subject_id',
         quantity=1,  # 'zero_or_one',
         doc="TODO: somehow inherit"
        )]
    )

    # TODO: add all of your new data types to this list
    new_data_types = [dandi_subject]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()

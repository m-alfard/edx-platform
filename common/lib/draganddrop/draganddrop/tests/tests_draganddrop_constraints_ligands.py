# -*- coding: utf-8 -*-
"""Complex chemistry tests for ligands."""

import unittest
import json

from ..draganddrop_constraints import get_all_dragabbles


class TestDragAndDropConstraintsLigands(unittest.TestCase):
    """Complex chemistry tests for ligands."""
    def test_ligands_general(self):
        xml = r"""
<customresponse>
    <html>
        <table style="width:665px; margin-left: auto; margin-right: auto;">
            <tr>
                <td style="width: 35px;">
                </td >
                <td style="width: 170px; text-align: center">
                    Free metal ion orbitals
                </td>
                <td style="width: 120px; text-align: center">
                    Octahedral complex ion orbitals \(ML_{6}^{n+}\)
                </td>
                <td style="width: 160px; text-align: center">
                    Ligand lone pair orbitals
                </td>
                <td >
                </td>
            </tr>
        </table>
    </html>

    <drag_and_drop_input img="/static/images/images_list/lcao-mo/lcao-template-ligands.png" target_outline="true" auto_resize="false" separate_labels="true">

        <!-- for middle side -->
        <draggable id="sigma_p_*" icon="/static/images/images_list/lcao-mo/orbital_triple.png" can_reuse="true" label="\(\sigma_{p}^{*}\)" >
            <target id="1" x="0" y="0" w="32" h="32"/>
            <target id="2" x="34" y="0" w="32" h="32"/>
            <target id="3" x="68" y="0" w="32" h="32"/>
        </draggable>

        <draggable id="sigma_s_*" icon="/static/images/images_list/lcao-mo/orbital_single.png" label="\(\sigma_{s}^{*}\)" can_reuse="true" >
            <target id="1" x="0" y="0" w="32" h="32"/>
        </draggable>

        <draggable id="e_g_*_label"  label="\( (e_{g}^{*}) \)" can_reuse="true" />

        <draggable id="e_g_*_1" icon="/static/images/images_list/lcao-mo/orbital_single.png" label="\( -d_{z}^{2} \)" can_reuse="true" >
            <target id="1" x="0" y="0" w="32" h="32"/>
        </draggable>
        <draggable id="e_g_*_2" icon="/static/images/images_list/lcao-mo/orbital_single.png" label="\( d_{x^{2}-y^{2}} \)" can_reuse="true" >
            <target id="1" x="0" y="0" w="32" h="32"/>
        </draggable>

        <draggable id="t2g_label"  label="\( (t_{2g}) \)" can_reuse="true" />

        <draggable id="d_xz" icon="/static/images/images_list/lcao-mo/orbital_single.png" label="\( d_{xz} \)" can_reuse="true" >
            <target id="1" x="0" y="0" w="32" h="32"/>
        </draggable>
        <draggable id="d_yz" icon="/static/images/images_list/lcao-mo/orbital_single.png" label="\( d_{yz} \)" can_reuse="true" >
            <target id="1" x="0" y="0" w="32" h="32"/>
        </draggable>
        <draggable id="d_xy" icon="/static/images/images_list/lcao-mo/orbital_single.png" label="\( d_{xy} \)" can_reuse="true" >
            <target id="1" x="0" y="0" w="32" h="32"/>
        </draggable>

        <draggable id="sigma_d" icon="/static/images/images_list/lcao-mo/orbital_double.png" label="\(\sigma_{d}\)" can_reuse="true" >
            <target id="1" x="0" y="0" w="32" h="32"/>
            <target id="2" x="34" y="0" w="32" h="32"/>
        </draggable>

        <draggable id="sigma_p" icon="/static/images/images_list/lcao-mo/orbital_triple.png" can_reuse="true" label="\(\sigma_{p}\)" >
            <target id="1" x="0" y="0" w="32" h="32"/>
            <target id="2" x="34" y="0" w="32" h="32"/>
            <target id="3" x="68" y="0" w="32" h="32"/>
        </draggable>

        <draggable id="sigma_s" icon="/static/images/images_list/lcao-mo/orbital_single.png" label="\(\sigma_{s}\)" can_reuse="true" >
            <target id="1" x="0" y="0" w="32" h="32"/>
        </draggable>

        <!-- for right side -->
        <draggable id="ligands" icon="/static/images/images_list/lcao-mo/orbital_five.png" can_reuse="true" >
            <target id="1" x="0" y="0" w="32" h="32"/>
            <target id="2" x="34" y="0" w="32" h="32"/>
            <target id="3" x="68" y="0" w="32" h="32"/>
            <target id="4" x="102" y="0" w="32" h="32"/>
            <target id="5" x="136" y="0" w="32" h="32"/>
        </draggable>

        <!-- for left side -->
        <draggable id="3d" icon="/static/images/images_list/lcao-mo/orbital_five.png" label="\(3d\)" can_reuse="true" >
            <target id="1" x="0" y="0" w="32" h="32"/>
            <target id="2" x="34" y="0" w="32" h="32"/>
            <target id="3" x="68" y="0" w="32" h="32"/>
            <target id="4" x="102" y="0" w="32" h="32"/>
            <target id="5" x="136" y="0" w="32" h="32"/>
        </draggable>

        <draggable id="4p" icon="/static/images/images_list/lcao-mo/orbital_triple.png" can_reuse="true" label="\(4p\)" >
            <target id="1" x="0" y="0" w="32" h="32"/>
            <target id="2" x="34" y="0" w="32" h="32"/>
            <target id="3" x="68" y="0" w="32" h="32"/>
        </draggable>

        <draggable id="4s" icon="/static/images/images_list/lcao-mo/orbital_single.png" label="\(4s\)" can_reuse="true" >
            <target id="1" x="0" y="0" w="32" h="32"/>
        </draggable>

        <target id="left-side"       type="grid" x="50"  y="10" w="170" h="655" col="1" row="19" />
        <target id="center-left"     type="grid" x="232" y="10" w="34" h="655" col="1" row="19" />
        <target id="center-center"   type="grid" x="271" y="10" w="34" h="655" col="1" row="19" />
        <target id="center-right"    type="grid" x="310" y="10" w="34" h="655" col="1" row="19" />
        <target id="right-side"      type="grid" x="358 " y="10" w="170" h="655" col="1" row="19" />

    </drag_and_drop_input>

    <answer type="loncapa/python"><![CDATA[
# Do not remove this!
orbitals = draganddrop.get_all_dragabbles(submission[0], xml)

constraints = [
        # left side
        orbitals['3d'].on('left-side').count == orbitals['3d'].count == 1,  # 0 - rule ordinal number
        orbitals['4p'].on('left-side').count == orbitals['4p'].count == 1,  # 1
        orbitals['4s'].on('left-side').count == orbitals['4s'].count == 1,  # 2

        #right side
        orbitals['ligands'].on('right-side').count == orbitals['ligands'].count == 1,  # 3

        # center side
        orbitals['sigma_s'].on('center-left').count + orbitals['sigma_s'].on('center-center').count + orbitals['sigma_s'].on('center-right').count == orbitals['sigma_s'].count == 1,

        orbitals['sigma_p'].on('center-left').count + orbitals['sigma_p'].on('center-center').count + orbitals['sigma_p'].on('center-right').count == orbitals['sigma_p'].count == 1,

        orbitals['sigma_d'].on('center-left').count + orbitals['sigma_d'].on('center-center').count + orbitals['sigma_d'].on('center-right').count == orbitals['sigma_d'].count == 1,

        orbitals['d_xy'].on('center-left').count + orbitals['d_xy'].on('center-center').count + orbitals['d_xy'].on('center-right').count == orbitals['d_xy'].count == 1,

        orbitals['d_yz'].on('center-left').count + orbitals['d_yz'].on('center-center').count + orbitals['d_yz'].on('center-right').count == orbitals['d_yz'].count == 1,

        orbitals['d_xz'].on('center-left').count + orbitals['d_xz'].on('center-center').count + orbitals['d_xz'].on('center-right').count == orbitals['d_xz'].count == 1,

        orbitals['t2g_label'].on('center-left').count + orbitals['t2g_label'].on('center-center').count + orbitals['t2g_label'].on('center-right').count == orbitals['t2g_label'].count == 1,

        orbitals['e_g_*_label'].on('center-left').count + orbitals['e_g_*_label'].on('center-center').count + orbitals['e_g_*_label'].on('center-right').count == orbitals['e_g_*_label'].count == 1,

        orbitals['e_g_*_1'].on('center-left').count + orbitals['e_g_*_1'].on('center-center').count + orbitals['e_g_*_1'].on('center-right').count == orbitals['e_g_*_1'].count == 1,

        orbitals['e_g_*_2'].on('center-left').count + orbitals['e_g_*_2'].on('center-center').count + orbitals['e_g_*_2'].on('center-right').count == orbitals['e_g_*_2'].count == 1,

        # y axis growths down
        orbitals['3d'][0].y         < orbitals['sigma_d'][0].y,  # 11
        orbitals['sigma_d'][0].y    < orbitals['sigma_p'][0].y,
        orbitals['sigma_p'][0].y    < orbitals['sigma_s'][0].y,
        orbitals['3d'][0].y         < orbitals['ligands'][0].y,  # 14
        orbitals['ligands'][0].y    < orbitals['sigma_d'][0].y,
        orbitals['3d'][0].y         < orbitals['t2g_label'][0].y,  # 18
        orbitals['t2g_label'][0].y  < orbitals['ligands'][0].y,
        orbitals['4s'][0].y         < orbitals['3d'][0].y,  # 23
        orbitals['4p'][0].y         < orbitals['4s'][0].y,  # 24
        orbitals['sigma_s_*'][0].y  < orbitals['4p'][0].y,
        orbitals['sigma_p_*'][0].y  < orbitals['sigma_s_*'][0].y,
        orbitals['e_g_*_label'][0].y < orbitals['e_g_*_1'][0].y,
        orbitals['e_g_*_label'][0].y > orbitals['4p'][0].y,

        orbitals['e_g_*_1'][0].y == orbitals['e_g_*_2'][0].y == orbitals['4s'][0].y,
        orbitals['d_yz'][0].y == orbitals['d_xy'][0].y == orbitals['d_yz'][0].y == orbitals['3d'][0].y

]
if all(constraints):
    correct = ['correct']
else:
    correct = ['incorrect']
]]></answer>
</customresponse>
"""

        user_answer = json.dumps([
            {"4p": "left-side{0}{6}"},
            {"4s": "left-side{0}{8}"},
            {"3d": "left-side{0}{10}"},
            {"e_g_*_2": "center-left{0}{8}"},
            {"d_xz": "center-left{0}{10}"},
            {"sigma_p_*": "center-center{0}{3}"},
            {"sigma_s_*": "center-center{0}{5}"},
            {"e_g_*_label": "center-center{0}{7}"},
            {"d_yz": "center-center{0}{10}"},
            {"t2g_label": "center-center{0}{12}"},
            {"sigma_d": "center-center{0}{14}"},
            {"sigma_p": "center-center{0}{16}"},
            {"sigma_s": "center-center{0}{18}"},
            {"e_g_*_1": "center-right{0}{8}"},
            {"d_xy": "center-right{0}{10}"},
            {"ligands": "right-side{0}{13}"}
        ])

        orbitals = get_all_dragabbles(user_answer, xml)

        constraints = [
            # left side
            orbitals['3d'].on('left-side').count == orbitals['3d'].count == 1,  # 0 - rule ordinal number
            orbitals['4p'].on('left-side').count == orbitals['4p'].count == 1,  # 1
            orbitals['4s'].on('left-side').count == orbitals['4s'].count == 1,  # 2

            #right side
            orbitals['ligands'].on('right-side').count == orbitals['ligands'].count == 1,  # 3

            # center side
            orbitals['sigma_s'].on('center-left').count + orbitals['sigma_s'].on('center-center').count + orbitals['sigma_s'].on('center-right').count == orbitals['sigma_s'].count == 1,

            orbitals['sigma_p'].on('center-left').count + orbitals['sigma_p'].on('center-center').count + orbitals['sigma_p'].on('center-right').count == orbitals['sigma_p'].count == 1,

            orbitals['sigma_d'].on('center-left').count + orbitals['sigma_d'].on('center-center').count + orbitals['sigma_d'].on('center-right').count == orbitals['sigma_d'].count == 1,

            orbitals['d_xy'].on('center-left').count + orbitals['d_xy'].on('center-center').count + orbitals['d_xy'].on('center-right').count == orbitals['d_xy'].count == 1,

            orbitals['d_yz'].on('center-left').count + orbitals['d_yz'].on('center-center').count + orbitals['d_yz'].on('center-right').count == orbitals['d_yz'].count == 1,

            orbitals['d_xz'].on('center-left').count + orbitals['d_xz'].on('center-center').count + orbitals['d_xz'].on('center-right').count == orbitals['d_xz'].count == 1,

            orbitals['t2g_label'].on('center-left').count + orbitals['t2g_label'].on('center-center').count + orbitals['t2g_label'].on('center-right').count == orbitals['t2g_label'].count == 1,

            orbitals['e_g_*_label'].on('center-left').count + orbitals['e_g_*_label'].on('center-center').count + orbitals['e_g_*_label'].on('center-right').count == orbitals['e_g_*_label'].count == 1,

            orbitals['e_g_*_1'].on('center-left').count + orbitals['e_g_*_1'].on('center-center').count + orbitals['e_g_*_1'].on('center-right').count == orbitals['e_g_*_1'].count == 1,

            orbitals['e_g_*_2'].on('center-left').count + orbitals['e_g_*_2'].on('center-center').count + orbitals['e_g_*_2'].on('center-right').count == orbitals['e_g_*_2'].count == 1,

            # y axis growths down
            orbitals['3d'][0].y < orbitals['sigma_d'][0].y,  # 11
            orbitals['sigma_d'][0].y < orbitals['sigma_p'][0].y,
            orbitals['sigma_p'][0].y < orbitals['sigma_s'][0].y,
            orbitals['3d'][0].y < orbitals['ligands'][0].y,  # 14
            orbitals['ligands'][0].y < orbitals['sigma_d'][0].y,
            orbitals['3d'][0].y < orbitals['t2g_label'][0].y,  # 18
            orbitals['t2g_label'][0].y < orbitals['ligands'][0].y,
            orbitals['4s'][0].y < orbitals['3d'][0].y,  # 23
            orbitals['4p'][0].y < orbitals['4s'][0].y,  # 24
            orbitals['sigma_s_*'][0].y < orbitals['4p'][0].y,
            orbitals['sigma_p_*'][0].y < orbitals['sigma_s_*'][0].y,
            orbitals['e_g_*_label'][0].y < orbitals['e_g_*_1'][0].y,
            orbitals['e_g_*_label'][0].y > orbitals['4p'][0].y,

            orbitals['e_g_*_1'][0].y == orbitals['e_g_*_2'][0].y == orbitals['4s'][0].y,
            orbitals['d_yz'][0].y == orbitals['d_xy'][0].y == orbitals['d_yz'][0].y == orbitals['3d'][0].y,
        ]
        self.assertEqual(all(constraints), True)
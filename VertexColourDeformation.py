import maya.cmds as cmds

def apply_vert_colours():
    selected = cmds.ls(selection=True)
    source_mesh = selected[0]
    target_mesh = selected[1]

    # Get the vertex positions of the source mesh in world space
    source_vertices_flat = cmds.xform(source_mesh + ".vtx[*]", q=True, ws=True, t=True)

    # xform returns a flat list [x1, y1, z1, x2, y2, z2, ...], so reshape it
    source_vertices = [
        (source_vertices_flat[i], source_vertices_flat[i+1], source_vertices_flat[i+2])
        for i in range(0, len(source_vertices_flat), 3)
    ]

    num_source_vertices = len(source_vertices)

    # Calculate the min and max difference values for each component
    min_diff = [999999.0, 999999.0, 999999.0]
    max_diff = [-999999.0, -999999.0, -999999.0]

    target_positions = []

    for i in range(num_source_vertices):
        source_pos = source_vertices[i]

        target_flat = cmds.xform(f"{target_mesh}.vtx[{i}]", q=True, ws=True, t=True)
        target_pos = (target_flat[0], target_flat[1], target_flat[2])
        target_positions.append(target_pos)

        diff = (
            target_pos[0] - source_pos[0],
            target_pos[1] - source_pos[1],
            target_pos[2] - source_pos[2]
        )

        for axis in range(3):
            min_diff[axis] = min(min_diff[axis], diff[axis])
            max_diff[axis] = max(max_diff[axis], diff[axis])

    # Loop through each vertex and apply vertex colours
    for i in range(num_source_vertices):
        source_pos = source_vertices[i]
        target_pos = target_positions[i]

        diff = (
            target_pos[0] - source_pos[0],
            target_pos[1] - source_pos[1],
            target_pos[2] - source_pos[2]
        )

        # Remap the position difference values to a normalised range
        rgb = []
        for axis, diff_val in enumerate(diff):
            diff_range = max_diff[axis] - min_diff[axis]
            if diff_val != 0 and diff_range != 0:
                rgb.append((diff_val - min_diff[axis]) / diff_range)
            else:
                rgb.append(0.5)

        cmds.polyColorPerVertex(
            f"{target_mesh}.vtx[{i}]",
            rgb=(rgb[0], rgb[1], rgb[2])
        )

apply_vert_colours()
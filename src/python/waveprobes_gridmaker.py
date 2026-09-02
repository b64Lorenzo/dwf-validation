#!/usr/bin/env python3
"""
Generate:
    waveprobes.xmfh
    waveprobe_channels.xmfh

Probe grid around vessel:
    x = every 1 m
    y = every 1 m

The hull interior is skipped.

Adjust the values below only.
"""

# --------------------------------------------------
# USER SETTINGS
# --------------------------------------------------

GRID_SPACING = 1.0

# extend probe field this far from hull
OUTER_MARGIN = 50.0

# logger quantities
QUANTITIES = {
    "zeta": "WaveElev",
    #"velocity": "WaveVelocity",
    #"meandir": "WaveMeanDir",
    #"p": "Pressure",
}

# --------------------------------------------------
# FILE GENERATION
# --------------------------------------------------

probe_file = open("wavesProbes_portfull_1m.xmfh", "w")
channel_file = open("waveProbes_portfull_1m_anysim.xmfh", "w")

probe_file.write("// Automatically generated\n\n")
channel_file.write("// Automatically generated\n\n")

# vessel envelope
#
# x:
#   -2*halfHydCenter_x
#   +2*halfHydCenter_x
#
# y:
#   -halfBeam
#   +halfBeam
#
# probes generated outside this area

max_x = 150
max_y = 70

for x in range(-max_x, max_x + 1):
    for y in range(20, max_y + 1):

        probe_name = f"probe_x{x:+d}_y{y:+d}"

        safe_name = (
            probe_name
            .replace("+", "p")
            .replace("-", "m")
        )

        # ------------------------------------------
        # Probe definition
        # ------------------------------------------

        probe_file.write(
f'''xsf::WaveProbe "{probe_name}" {{
    position = {{
        option::ships::HydCenter_x + ({x}),
        option::ships::halfBeam + {y},
        option::logger::waveProbes_z
    }};
}};

'''
        )

        # ------------------------------------------
        # Logger channels
        # ------------------------------------------

        for quantity, prefix in QUANTITIES.items():

            channel_file.write(
f'''ref::channels = "*/*/{probe_name}, {quantity}, {prefix}_{safe_name}";
'''
            )

probe_file.close()
channel_file.close()

print("Created:")
print("  waveprobes.xmfh")
print("  waveprobe_channels.xmfh")
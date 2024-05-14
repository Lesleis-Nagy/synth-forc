import matplotlib.patches as patches
import matplotlib.pyplot as plt

from synth_forc.synthforc_db import SynthForcDB


def main():

    db = SynthForcDB("/Users/lnagy2/Data/forc-paper-zenodo/synth-forc-data.db")

    major_loop = db.get_major_loop_by_aspect_ratio_and_size(2.75, 100)

    b_up = major_loop["B"].to_list()
    m_up = major_loop["M"].to_list()

    up = list(zip(b_up, m_up))

    b_down = list(reversed(b_up))
    m_down = [-1.0 * m for m in m_up]

    down = list(reversed(list(zip(b_down, m_down))))

    # Fix trapezoids for right-hand winding.
    trapezoids = [((b2, m2), (b4, m4), (b3, m3), (b1, m1)) for
                  ((b1, m1), (b2, m2)), ((b3, m3), (b4, m4)) in
                  zip(zip(up, up[1:]), zip(down, down[1:]))]

    fig, ax = plt.subplots()
    ax.set_xlabel("B (T)")
    ax.set_ylabel("M (A/m)")

    ax.scatter(b_up, m_up, c="black", s=0.4)
    ax.scatter(b_down, m_down, c="red", s=0.4)

    ax.plot(b_up, m_up, c="black", linewidth=0.2)
    ax.plot(b_down, m_down, c="red", linewidth=0.2)

    area = 0.0
    for trapezoid in trapezoids:
        print(trapezoid)
        ax.add_patch(patches.Polygon(xy=trapezoid, fill=False, linewidth=0.2, edgecolor="blue"))
        area += quadrilateral_area(trapezoid[0], trapezoid[1], trapezoid[2], trapezoid[3])

    print(f"Loop area: {area}")

    fig.savefig("loop.pdf")
    plt.close()


def quadrilateral_area(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    return 0.5 * ((x1 * y2 + x2 * y3 + x3 * y4 + x4 * y1) - (x2 * y1 + x3 * y2 + x4 * y3 + x1 * y4))


if __name__ == "__main__":
    main()

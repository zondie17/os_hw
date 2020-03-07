#include <iostream>
int main() {
    const int PDBR = 0x6c;
    int vir = 0x1e6f;
    int page[128][32];
    int disk[128][32];

    freopen("../page.txt", "r", stdin);
    for (auto & i : page)
        for (int & j : i)
            scanf("%x", &j);
    fclose(stdin);
    freopen("../disk.txt", "r", stdin);
    for (auto & i : disk)
        for (int & j : i)
            scanf("%x", &j);
    fclose(stdin);

    int pde = vir >> 10 & 0b11111;
    int pte = vir >> 5 & 0b11111;
    int lst = vir & 0b11111;
    int value = -1;
    int pde_contents = -1;
    int pde_1 = -1;
    int pde_7 = -1;
    int pte_contents = -1;
    int pte_1 = -1;
    int pte_7 = -1;
    int add = -1;
    bool phy = false; //true is phy add, false is disk add
    pde_contents = page[PDBR][pde];
    if (pde_contents != 0x7f) {
        pde_1 = pde_contents >> 7 & 0b1;
        if (pde_1) {
            pde_7 = pde_contents & 0b1111111;
            pte_contents = page[pde_7][pte];
            pte_1 = pte_contents >> 7 & 0b1;
            pte_7 = pte_contents & 0b1111111;
            if (pte_1) {
                value = page[pte_7][lst];
                phy = true;
            }
            else
                value = disk[pte_7][lst];
            add = (pte_7 << 5) + lst;
        }
    }

    printf("pde index: 0x%02x\n", pde);
    printf("pde contents: 0x%02x\n", pde_contents);
    printf("pte index: 0x%02x\n", pte);
    printf("pte contents: 0x%02x\n", pte_contents);
    printf("value: 0x%02x\n", value);
    if (phy)
        printf("Physical Address: 0x%03x\n", add);
    else
        printf("Disk Sector Address: 0x%03x\n", add);

    return 0;
}
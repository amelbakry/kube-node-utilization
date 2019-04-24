# Kubernetes Node Utilization

This is simple python script to get actual utilization of kubernetes nodes (worker and master)

Note: node names are already modified

```bash
Kubernetes Node Utilization.......... 
+------------------------------------------------+--------+--------+
| NodeName                                       | CPU    | Memory |
+------------------------------------------------+--------+--------+
| ip-176-35-32-139.eu-central-1.compute.internal | 13.49% | 60.87% |
| ip-176-35-26-21.eu-central-1.compute.internal  | 5.89%  | 15.10% |
| ip-176-35-28-29.eu-central-1.compute.internal  | 22.79% | 30.34% |
| ip-176-35-4-167.eu-central-1.compute.internal  | 11.63% | 39.49% |
| ip-176-35-17-237.eu-central-1.compute.internal | 8.32%  | 25.69% |
| ip-176-35-8-237.eu-central-1.compute.internal  | 5.15%  | 28.78% |
| ip-176-35-8-237.eu-central-1.compute.internal  | 6.91%  | 46.01% |
| ip-176-35-0-89.eu-central-1.compute.internal   | 3.59%  | 11.49% |
| ip-176-35-10-120.eu-central-1.compute.internal | 21.19% | 44.44% |
| ip-176-35-7-90.eu-central-1.compute.internal   | 5.53%  | 20.84% |
| ip-176-35-6-117.eu-central-1.compute.internal  | 6.21%  | 19.59% |
| ip-176-35-18-150.eu-central-1.compute.internal | 2.68%  | 11.10% |
| ip-176-35-4-128.eu-central-1.compute.internal  | 4.44%  | 17.46% |
| ip-176-35-9-122.eu-central-1.compute.internal  | 8.08%  | 65.51% |
| ip-176-35-22-243.eu-central-1.compute.internal | 6.29%  | 19.28% |
| ip-176-35-4-216.eu-central-1.compute.internal  | 68.89% | 56.30% |
| ip-176-35-13-48.eu-central-1.compute.internal  | 7.03%  | 53.98% |
| ip-176-35-19-57.eu-central-1.compute.internal  | 3.77%  | 9.28%  |
| ip-176-35-7-121.eu-central-1.compute.internal  | 3.82%  | 11.81% |
| ip-176-35-8-59.eu-central-1.compute.internal   | 12.47% | 60.03% |
| ip-176-35-12-135.eu-central-1.compute.internal | 12.18% | 63.57% |
| ip-176-35-16-203.eu-central-1.compute.internal | 3.49%  | 28.76% |
| ip-176-35-7-197.eu-central-1.compute.internal  | 4.83%  | 14.87% |
+------------------------------------------------+--------+--------+
```

If you need the utilization based on requests and limits

```bash
└─ $ ▶ zkubectl describe node | grep -A4 "Allocated"
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource                    Requests       Limits
  --------                    --------       ------
  cpu                         7757m (99%)    6907m (88%)
--
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource                    Requests           Limits
  --------                    --------           ------
  cpu                         7698m (98%)        28043m (359%)
--
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource                    Requests       Limits
  --------                    --------       ------
  cpu                         3797m (99%)    23487m (618%)
--
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource                    Requests       Limits
  --------                    --------       ------
  cpu                         7797m (99%)    63362m (812%)
--
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource                    Requests       Limits
  --------                    --------       ------
  cpu                         3792m (99%)    39082m (1028%)
--
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource                    Requests       Limits
  --------                    --------       ------
  cpu                         7692m (98%)    5892m (75%)
--
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource                    Requests      Limits
  --------                    --------      ------
  cpu                         3782m (99%)   3982m (104%)
--
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource                    Requests       Limits
  --------                    --------       ------
  cpu                         7732m (99%)    7707m (98%)
```

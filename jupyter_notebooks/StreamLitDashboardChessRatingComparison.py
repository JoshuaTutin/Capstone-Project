#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from io import StringIO

# ===============================
# Load CSV from string
# ===============================
csv_data = """time_control_lichess,percentile,rating_lichess,time_control_fide,rating_fide,lichess_tc,fide_tc
bullet,0.01,811.0,Blitz,1410.0,bullet,Blitz
bullet,0.02,885.0,Blitz,1419.0,bullet,Blitz
bullet,0.03,937.0,Blitz,1426.0,bullet,Blitz
bullet,0.04,975.0,Blitz,1432.0,bullet,Blitz
bullet,0.05,1012.1000000000001,Blitz,1439.0,bullet,Blitz
bullet,0.060000000000000005,1041.0,Blitz,1446.0,bullet,Blitz
bullet,0.06999999999999999,1066.9399999999996,Blitz,1452.0,bullet,Blitz
bullet,0.08,1093.0,Blitz,1458.0,bullet,Blitz
bullet,0.09,1115.7799999999997,Blitz,1463.0,bullet,Blitz
bullet,0.09999999999999999,1139.0,Blitz,1470.0,bullet,Blitz
bullet,0.11,1158.0,Blitz,1475.0,bullet,Blitz
bullet,0.12,1180.0,Blitz,1481.0,bullet,Blitz
bullet,0.13,1200.0,Blitz,1486.0,bullet,Blitz
bullet,0.14,1219.0,Blitz,1491.0,bullet,Blitz
bullet,0.15000000000000002,1237.0,Blitz,1496.0,bullet,Blitz
bullet,0.16,1255.0,Blitz,1501.0,bullet,Blitz
bullet,0.17,1272.0,Blitz,1506.0,bullet,Blitz
bullet,0.18000000000000002,1289.0,Blitz,1510.0,bullet,Blitz
bullet,0.19,1304.0,Blitz,1516.0,bullet,Blitz
bullet,0.2,1320.0,Blitz,1520.0,bullet,Blitz
bullet,0.21000000000000002,1335.0,Blitz,1525.0,bullet,Blitz
bullet,0.22,1349.2399999999998,Blitz,1531.0,bullet,Blitz
bullet,0.23,1365.0,Blitz,1536.0,bullet,Blitz
bullet,0.24000000000000002,1380.0,Blitz,1540.0,bullet,Blitz
bullet,0.25,1394.0,Blitz,1545.0,bullet,Blitz
bullet,0.26,1407.0,Blitz,1550.0,bullet,Blitz
bullet,0.27,1421.0,Blitz,1555.0,bullet,Blitz
bullet,0.28,1433.0,Blitz,1561.0,bullet,Blitz
bullet,0.29000000000000004,1448.0,Blitz,1566.0,bullet,Blitz
bullet,0.3,1460.6000000000004,Blitz,1571.0,bullet,Blitz
bullet,0.31,1474.0,Blitz,1576.0,bullet,Blitz
bullet,0.32,1486.0,Blitz,1581.0,bullet,Blitz
bullet,0.33,1500.0,Blitz,1586.0,bullet,Blitz
bullet,0.34,1502.0,Blitz,1591.0,bullet,Blitz
bullet,0.35000000000000003,1513.0,Blitz,1595.0,bullet,Blitz
bullet,0.36000000000000004,1527.0,Blitz,1601.0,bullet,Blitz
bullet,0.37,1539.0,Blitz,1606.0,bullet,Blitz
bullet,0.38,1551.0,Blitz,1611.0,bullet,Blitz
bullet,0.39,1562.0,Blitz,1617.0,bullet,Blitz
bullet,0.4,1573.0,Blitz,1621.0,bullet,Blitz
bullet,0.41000000000000003,1584.0,Blitz,1627.0,bullet,Blitz
bullet,0.42000000000000004,1596.0,Blitz,1632.0,bullet,Blitz
bullet,0.43,1608.0,Blitz,1637.0,bullet,Blitz
bullet,0.44,1620.0,Blitz,1642.0,bullet,Blitz
bullet,0.45,1631.0,Blitz,1647.0,bullet,Blitz
bullet,0.46,1643.0,Blitz,1652.0,bullet,Blitz
bullet,0.47000000000000003,1654.0,Blitz,1658.0,bullet,Blitz
bullet,0.48000000000000004,1666.0,Blitz,1664.0,bullet,Blitz
bullet,0.49,1676.0,Blitz,1670.0,bullet,Blitz
bullet,0.5,1688.0,Blitz,1675.0,bullet,Blitz
bullet,0.51,1700.0,Blitz,1681.0,bullet,Blitz
bullet,0.52,1711.0,Blitz,1687.0,bullet,Blitz
bullet,0.53,1722.0,Blitz,1693.0,bullet,Blitz
bullet,0.54,1733.0,Blitz,1699.0,bullet,Blitz
bullet,0.55,1745.0,Blitz,1705.0,bullet,Blitz
bullet,0.56,1757.0,Blitz,1710.0,bullet,Blitz
bullet,0.5700000000000001,1768.0,Blitz,1716.0,bullet,Blitz
bullet,0.5800000000000001,1779.0,Blitz,1720.0,bullet,Blitz
bullet,0.59,1791.0,Blitz,1727.0,bullet,Blitz
bullet,0.6,1803.0,Blitz,1734.0,bullet,Blitz
bullet,0.61,1813.0,Blitz,1739.0,bullet,Blitz
bullet,0.62,1823.0,Blitz,1745.0,bullet,Blitz
bullet,0.63,1834.0,Blitz,1752.0,bullet,Blitz
bullet,0.64,1846.0,Blitz,1758.0,bullet,Blitz
bullet,0.65,1858.0,Blitz,1765.0,bullet,Blitz
bullet,0.66,1870.0,Blitz,1772.0,bullet,Blitz
bullet,0.67,1881.140000000003,Blitz,1779.0,bullet,Blitz
bullet,0.68,1894.0,Blitz,1785.0,bullet,Blitz
bullet,0.6900000000000001,1907.0,Blitz,1792.0,bullet,Blitz
bullet,0.7000000000000001,1918.0,Blitz,1799.0,bullet,Blitz
bullet,0.7100000000000001,1928.0,Blitz,1807.0,bullet,Blitz
bullet,0.72,1940.0,Blitz,1814.0,bullet,Blitz
bullet,0.73,1953.0,Blitz,1821.0,bullet,Blitz
bullet,0.74,1966.0,Blitz,1827.0,bullet,Blitz
bullet,0.75,1979.0,Blitz,1834.0,bullet,Blitz
bullet,0.76,1991.0,Blitz,1842.0,bullet,Blitz
bullet,0.77,2005.0,Blitz,1851.0,bullet,Blitz
bullet,0.78,2017.0,Blitz,1858.0,bullet,Blitz
bullet,0.79,2032.0,Blitz,1866.0,bullet,Blitz
bullet,0.8,2046.0,Blitz,1875.0,bullet,Blitz
bullet,0.81,2061.0,Blitz,1883.0,bullet,Blitz
bullet,0.8200000000000001,2076.0,Blitz,1893.0,bullet,Blitz
bullet,0.8300000000000001,2091.0,Blitz,1902.0,bullet,Blitz
bullet,0.8400000000000001,2107.0,Blitz,1911.0,bullet,Blitz
bullet,0.85,2123.0,Blitz,1921.0,bullet,Blitz
bullet,0.86,2140.0,Blitz,1930.7599999999984,bullet,Blitz
bullet,0.87,2157.0,Blitz,1942.0,bullet,Blitz
bullet,0.88,2176.0,Blitz,1953.0,bullet,Blitz
bullet,0.89,2197.0,Blitz,1962.0,bullet,Blitz
bullet,0.9,2217.0,Blitz,1975.0,bullet,Blitz
bullet,0.91,2238.220000000001,Blitz,1992.0,bullet,Blitz
bullet,0.92,2262.0,Blitz,2010.0,bullet,Blitz
bullet,0.93,2288.0,Blitz,2031.0,bullet,Blitz
bullet,0.9400000000000001,2314.0,Blitz,2054.0,bullet,Blitz
bullet,0.9500000000000001,2345.0,Blitz,2086.2000000000007,bullet,Blitz
bullet,0.9600000000000001,2386.0,Blitz,2119.360000000004,bullet,Blitz
bullet,0.97,2430.0,Blitz,2161.0,bullet,Blitz
bullet,0.98,2507.0,Blitz,2220.3600000000006,bullet,Blitz
bullet,0.99,2619.0,Blitz,2325.84,bullet,Blitz
bullet,1.0,3225.0,Blitz,2785.0,bullet,Blitz
blitz,0.01,754.0,Blitz,1410.0,blitz,Blitz
blitz,0.02,827.0,Blitz,1419.0,blitz,Blitz
blitz,0.03,881.0,Blitz,1426.0,blitz,Blitz
blitz,0.04,918.0,Blitz,1432.0,blitz,Blitz
blitz,0.05,949.0,Blitz,1439.0,blitz,Blitz
blitz,0.060000000000000005,977.0,Blitz,1446.0,blitz,Blitz
blitz,0.06999999999999999,1003.0,Blitz,1452.0,blitz,Blitz
blitz,0.08,1025.0,Blitz,1458.0,blitz,Blitz
blitz,0.09,1048.0,Blitz,1463.0,blitz,Blitz
blitz,0.09999999999999999,1069.6000000000004,Blitz,1470.0,blitz,Blitz
blitz,0.11,1089.0,Blitz,1475.0,blitz,Blitz
blitz,0.12,1108.0,Blitz,1481.0,blitz,Blitz
blitz,0.13,1126.0,Blitz,1486.0,blitz,Blitz
blitz,0.14,1144.0,Blitz,1491.0,blitz,Blitz
blitz,0.15000000000000002,1160.0,Blitz,1496.0,blitz,Blitz
blitz,0.16,1178.0,Blitz,1501.0,blitz,Blitz
blitz,0.17,1193.0,Blitz,1506.0,blitz,Blitz
blitz,0.18000000000000002,1208.0,Blitz,1510.0,blitz,Blitz
blitz,0.19,1223.0,Blitz,1516.0,blitz,Blitz
blitz,0.2,1236.0,Blitz,1520.0,blitz,Blitz
blitz,0.21000000000000002,1251.0,Blitz,1525.0,blitz,Blitz
blitz,0.22,1264.0,Blitz,1531.0,blitz,Blitz
blitz,0.23,1278.0,Blitz,1536.0,blitz,Blitz
blitz,0.24000000000000002,1291.0,Blitz,1540.0,blitz,Blitz
blitz,0.25,1305.0,Blitz,1545.0,blitz,Blitz
blitz,0.26,1317.0,Blitz,1550.0,blitz,Blitz
blitz,0.27,1329.0,Blitz,1555.0,blitz,Blitz
blitz,0.28,1341.0,Blitz,1561.0,blitz,Blitz
blitz,0.29000000000000004,1352.0,Blitz,1566.0,blitz,Blitz
blitz,0.3,1363.0,Blitz,1571.0,blitz,Blitz
blitz,0.31,1375.0,Blitz,1576.0,blitz,Blitz
blitz,0.32,1386.0,Blitz,1581.0,blitz,Blitz
blitz,0.33,1396.0,Blitz,1586.0,blitz,Blitz
blitz,0.34,1407.0,Blitz,1591.0,blitz,Blitz
blitz,0.35000000000000003,1417.0,Blitz,1595.0,blitz,Blitz
blitz,0.36000000000000004,1428.0,Blitz,1601.0,blitz,Blitz
blitz,0.37,1439.0,Blitz,1606.0,blitz,Blitz
blitz,0.38,1450.0,Blitz,1611.0,blitz,Blitz
blitz,0.39,1460.0,Blitz,1617.0,blitz,Blitz
blitz,0.4,1471.0,Blitz,1621.0,blitz,Blitz
blitz,0.41000000000000003,1482.0,Blitz,1627.0,blitz,Blitz
blitz,0.42000000000000004,1492.0,Blitz,1632.0,blitz,Blitz
blitz,0.43,1500.0,Blitz,1637.0,blitz,Blitz
blitz,0.44,1507.0,Blitz,1642.0,blitz,Blitz
blitz,0.45,1517.0,Blitz,1647.0,blitz,Blitz
blitz,0.46,1528.0,Blitz,1652.0,blitz,Blitz
blitz,0.47000000000000003,1538.0,Blitz,1658.0,blitz,Blitz
blitz,0.48000000000000004,1548.0,Blitz,1664.0,blitz,Blitz
blitz,0.49,1558.0,Blitz,1670.0,blitz,Blitz
blitz,0.5,1568.0,Blitz,1675.0,blitz,Blitz
blitz,0.51,1578.0,Blitz,1681.0,blitz,Blitz
blitz,0.52,1587.0,Blitz,1687.0,blitz,Blitz
blitz,0.53,1597.0,Blitz,1693.0,blitz,Blitz
blitz,0.54,1607.0,Blitz,1699.0,blitz,Blitz
blitz,0.55,1617.0,Blitz,1705.0,blitz,Blitz
blitz,0.56,1627.0,Blitz,1710.0,blitz,Blitz
blitz,0.5700000000000001,1638.0,Blitz,1716.0,blitz,Blitz
blitz,0.5800000000000001,1647.0,Blitz,1720.0,blitz,Blitz
blitz,0.59,1658.0,Blitz,1727.0,blitz,Blitz
blitz,0.6,1667.0,Blitz,1734.0,blitz,Blitz
blitz,0.61,1677.0,Blitz,1739.0,blitz,Blitz
blitz,0.62,1688.0,Blitz,1745.0,blitz,Blitz
blitz,0.63,1698.0,Blitz,1752.0,blitz,Blitz
blitz,0.64,1708.0,Blitz,1758.0,blitz,Blitz
blitz,0.65,1719.0,Blitz,1765.0,blitz,Blitz
blitz,0.66,1729.0,Blitz,1772.0,blitz,Blitz
blitz,0.67,1739.0,Blitz,1779.0,blitz,Blitz
blitz,0.68,1750.0,Blitz,1785.0,blitz,Blitz
blitz,0.6900000000000001,1760.0,Blitz,1792.0,blitz,Blitz
blitz,0.7000000000000001,1770.0,Blitz,1799.0,blitz,Blitz
blitz,0.7100000000000001,1780.0,Blitz,1807.0,blitz,Blitz
blitz,0.72,1791.0,Blitz,1814.0,blitz,Blitz
blitz,0.73,1802.0,Blitz,1821.0,blitz,Blitz
blitz,0.74,1812.0,Blitz,1827.0,blitz,Blitz
blitz,0.75,1822.0,Blitz,1834.0,blitz,Blitz
blitz,0.76,1833.0,Blitz,1842.0,blitz,Blitz
blitz,0.77,1845.0,Blitz,1851.0,blitz,Blitz
blitz,0.78,1857.0,Blitz,1858.0,blitz,Blitz
blitz,0.79,1869.0,Blitz,1866.0,blitz,Blitz
blitz,0.8,1881.0,Blitz,1875.0,blitz,Blitz
blitz,0.81,1893.0,Blitz,1883.0,blitz,Blitz
blitz,0.8200000000000001,1906.0,Blitz,1893.0,blitz,Blitz
blitz,0.8300000000000001,1919.0,Blitz,1902.0,blitz,Blitz
blitz,0.8400000000000001,1932.0,Blitz,1911.0,blitz,Blitz
blitz,0.85,1946.0999999999985,Blitz,1921.0,blitz,Blitz
blitz,0.86,1960.0,Blitz,1930.7599999999984,blitz,Blitz
blitz,0.87,1975.0,Blitz,1942.0,blitz,Blitz
blitz,0.88,1992.0,Blitz,1953.0,blitz,Blitz
blitz,0.89,2008.0,Blitz,1962.0,blitz,Blitz
blitz,0.9,2025.4000000000015,Blitz,1975.0,blitz,Blitz
blitz,0.91,2044.0,Blitz,1992.0,blitz,Blitz
blitz,0.92,2064.0,Blitz,2010.0,blitz,Blitz
blitz,0.93,2087.0,Blitz,2031.0,blitz,Blitz
blitz,0.9400000000000001,2113.0,Blitz,2054.0,blitz,Blitz
blitz,0.9500000000000001,2140.0,Blitz,2086.2000000000007,blitz,Blitz
blitz,0.9600000000000001,2173.0,Blitz,2119.360000000004,blitz,Blitz
blitz,0.97,2215.0,Blitz,2161.0,blitz,Blitz
blitz,0.98,2270.0,Blitz,2220.3600000000006,blitz,Blitz
blitz,0.99,2358.0,Blitz,2325.84,blitz,Blitz
blitz,1.0,3080.0,Blitz,2785.0,blitz,Blitz
rapid,0.01,686.0,Rapid,1408.0,rapid,Rapid
rapid,0.02,762.7,Rapid,1414.0,rapid,Rapid
rapid,0.03,814.05,Rapid,1420.0,rapid,Rapid
rapid,0.04,854.0,Rapid,1425.0,rapid,Rapid
rapid,0.05,885.0,Rapid,1431.0,rapid,Rapid
rapid,0.060000000000000005,913.0,Rapid,1436.0,rapid,Rapid
rapid,0.06999999999999999,939.0,Rapid,1441.0,rapid,Rapid
rapid,0.08,961.0,Rapid,1446.0,rapid,Rapid
rapid,0.09,982.0,Rapid,1450.0,rapid,Rapid
rapid,0.09999999999999999,1002.0,Rapid,1455.0,rapid,Rapid
rapid,0.11,1019.0,Rapid,1459.0,rapid,Rapid
rapid,0.12,1034.0,Rapid,1463.0,rapid,Rapid
rapid,0.13,1052.0,Rapid,1468.0,rapid,Rapid
rapid,0.14,1070.0,Rapid,1472.0,rapid,Rapid
rapid,0.15000000000000002,1087.0,Rapid,1476.0,rapid,Rapid
rapid,0.16,1103.0,Rapid,1481.0,rapid,Rapid
rapid,0.17,1119.0,Rapid,1485.0,rapid,Rapid
rapid,0.18000000000000002,1134.0,Rapid,1489.0,rapid,Rapid
rapid,0.19,1148.0,Rapid,1493.0,rapid,Rapid
rapid,0.2,1164.0,Rapid,1497.0,rapid,Rapid
rapid,0.21000000000000002,1177.0,Rapid,1501.0,rapid,Rapid
rapid,0.22,1191.0,Rapid,1505.0,rapid,Rapid
rapid,0.23,1203.0,Rapid,1509.0,rapid,Rapid
rapid,0.24000000000000002,1214.4000000000015,Rapid,1513.0,rapid,Rapid
rapid,0.25,1227.75,Rapid,1517.0,rapid,Rapid
rapid,0.26,1239.1000000000004,Rapid,1521.0,rapid,Rapid
rapid,0.27,1252.0,Rapid,1525.0,rapid,Rapid
rapid,0.28,1264.0,Rapid,1530.0,rapid,Rapid
rapid,0.29000000000000004,1276.0,Rapid,1534.0,rapid,Rapid
rapid,0.3,1288.0,Rapid,1538.0,rapid,Rapid
rapid,0.31,1298.0,Rapid,1542.0,rapid,Rapid
rapid,0.32,1309.2000000000007,Rapid,1547.0,rapid,Rapid
rapid,0.33,1322.0,Rapid,1551.0,rapid,Rapid
rapid,0.34,1333.0,Rapid,1556.0,rapid,Rapid
rapid,0.35000000000000003,1343.0,Rapid,1561.0,rapid,Rapid
rapid,0.36000000000000004,1354.0,Rapid,1565.0,rapid,Rapid
rapid,0.37,1365.0,Rapid,1570.0,rapid,Rapid
rapid,0.38,1376.0,Rapid,1574.0,rapid,Rapid
rapid,0.39,1387.0,Rapid,1578.0,rapid,Rapid
rapid,0.4,1397.0,Rapid,1583.0,rapid,Rapid
rapid,0.41000000000000003,1407.0,Rapid,1588.0,rapid,Rapid
rapid,0.42000000000000004,1417.0,Rapid,1593.0,rapid,Rapid
rapid,0.43,1426.0,Rapid,1597.0,rapid,Rapid
rapid,0.44,1437.0,Rapid,1602.0,rapid,Rapid
rapid,0.45,1446.75,Rapid,1607.0,rapid,Rapid
rapid,0.46,1457.0,Rapid,1611.0,rapid,Rapid
rapid,0.47000000000000003,1468.0,Rapid,1616.0,rapid,Rapid
rapid,0.48000000000000004,1479.0,Rapid,1621.0,rapid,Rapid
rapid,0.49,1489.0,Rapid,1626.0,rapid,Rapid
rapid,0.5,1498.0,Rapid,1631.0,rapid,Rapid
rapid,0.51,1500.0,Rapid,1636.0,rapid,Rapid
rapid,0.52,1504.0,Rapid,1641.0,rapid,Rapid
rapid,0.53,1512.0,Rapid,1646.0,rapid,Rapid
rapid,0.54,1521.9000000000015,Rapid,1652.0,rapid,Rapid
rapid,0.55,1530.0,Rapid,1657.0,rapid,Rapid
rapid,0.56,1540.0,Rapid,1662.0,rapid,Rapid
rapid,0.5700000000000001,1549.0,Rapid,1667.0,rapid,Rapid
rapid,0.5800000000000001,1559.0,Rapid,1673.0,rapid,Rapid
rapid,0.59,1569.0,Rapid,1679.0,rapid,Rapid
rapid,0.6,1578.0,Rapid,1685.0,rapid,Rapid
rapid,0.61,1588.0,Rapid,1691.0,rapid,Rapid
rapid,0.62,1598.0,Rapid,1697.0,rapid,Rapid
rapid,0.63,1608.0,Rapid,1702.0,rapid,Rapid
rapid,0.64,1619.0,Rapid,1708.0,rapid,Rapid
rapid,0.65,1628.0,Rapid,1714.0,rapid,Rapid
rapid,0.66,1638.0,Rapid,1721.0,rapid,Rapid
rapid,0.67,1647.0,Rapid,1728.0,rapid,Rapid
rapid,0.68,1657.0,Rapid,1733.0,rapid,Rapid
rapid,0.6900000000000001,1667.0,Rapid,1739.0,rapid,Rapid
rapid,0.7000000000000001,1678.0,Rapid,1746.0,rapid,Rapid
rapid,0.7100000000000001,1689.0,Rapid,1752.0,rapid,Rapid
rapid,0.72,1700.0,Rapid,1759.0,rapid,Rapid
rapid,0.73,1710.0,Rapid,1766.0,rapid,Rapid
rapid,0.74,1722.0,Rapid,1773.0,rapid,Rapid
rapid,0.75,1732.0,Rapid,1780.0,rapid,Rapid
rapid,0.76,1742.0,Rapid,1788.0,rapid,Rapid
rapid,0.77,1753.0,Rapid,1796.0,rapid,Rapid
rapid,0.78,1764.0,Rapid,1804.0,rapid,Rapid
rapid,0.79,1776.0,Rapid,1813.0,rapid,Rapid
rapid,0.8,1788.0,Rapid,1821.0,rapid,Rapid
rapid,0.81,1800.0,Rapid,1830.0,rapid,Rapid
rapid,0.8200000000000001,1813.0,Rapid,1839.0,rapid,Rapid
rapid,0.8300000000000001,1825.0,Rapid,1849.0,rapid,Rapid
rapid,0.8400000000000001,1839.0,Rapid,1859.0,rapid,Rapid
rapid,0.85,1852.0,Rapid,1870.0,rapid,Rapid
rapid,0.86,1867.0,Rapid,1881.0,rapid,Rapid
rapid,0.87,1882.0,Rapid,1891.0,rapid,Rapid
rapid,0.88,1898.0,Rapid,1904.0,rapid,Rapid
rapid,0.89,1912.0,Rapid,1916.0,rapid,Rapid
rapid,0.9,1928.0,Rapid,1929.0,rapid,Rapid
rapid,0.91,1944.0,Rapid,1944.0,rapid,Rapid
rapid,0.92,1961.0,Rapid,1958.0,rapid,Rapid
rapid,0.93,1981.0,Rapid,1976.1200000000026,rapid,Rapid
rapid,0.9400000000000001,2005.0,Rapid,1997.9599999999991,rapid,Rapid
rapid,0.9500000000000001,2030.0,Rapid,2027.0,rapid,Rapid
rapid,0.9600000000000001,2060.0,Rapid,2062.0,rapid,Rapid
rapid,0.97,2100.0,Rapid,2107.0,rapid,Rapid
rapid,0.98,2148.2999999999993,Rapid,2168.0,rapid,Rapid
rapid,0.99,2224.0,Rapid,2262.16,rapid,Rapid
rapid,1.0,3096.0,Rapid,2735.0,rapid,Rapid
classical,0.01,863.36,Standard,1408.0,classical,Standard
classical,0.02,959.72,Standard,1416.0,classical,Standard
classical,0.03,1018.35,Standard,1423.0,classical,Standard
classical,0.04,1053.24,Standard,1429.0,classical,Standard
classical,0.05,1083.35,Standard,1435.0,classical,Standard
classical,0.060000000000000005,1103.0,Standard,1441.0,classical,Standard
classical,0.06999999999999999,1144.52,Standard,1446.0,classical,Standard
classical,0.08,1162.44,Standard,1452.0,classical,Standard
classical,0.09,1173.62,Standard,1456.0,classical,Standard
classical,0.09999999999999999,1185.9,Standard,1462.0,classical,Standard
classical,0.11,1201.99,Standard,1467.0,classical,Standard
classical,0.12,1226.08,Standard,1472.0,classical,Standard
classical,0.13,1241.17,Standard,1477.0,classical,Standard
classical,0.14,1250.52,Standard,1482.0,classical,Standard
classical,0.15000000000000002,1261.7,Standard,1488.0,classical,Standard
classical,0.16,1281.76,Standard,1492.0,classical,Standard
classical,0.17,1296.06,Standard,1498.0,classical,Standard
classical,0.18000000000000002,1309.6200000000001,Standard,1502.0,classical,Standard
classical,0.19,1320.71,Standard,1507.0,classical,Standard
classical,0.2,1331.8,Standard,1512.0,classical,Standard
classical,0.21000000000000002,1339.0,Standard,1517.0,classical,Standard
classical,0.22,1348.0,Standard,1522.0,classical,Standard
classical,0.23,1358.0,Standard,1526.0,classical,Standard
classical,0.24000000000000002,1366.3200000000002,Standard,1531.0,classical,Standard
classical,0.25,1375.5,Standard,1537.0,classical,Standard
classical,0.26,1384.0,Standard,1542.0,classical,Standard
classical,0.27,1398.43,Standard,1547.0,classical,Standard
classical,0.28,1412.52,Standard,1552.0,classical,Standard
classical,0.29000000000000004,1422.22,Standard,1557.0,classical,Standard
classical,0.3,1436.1,Standard,1562.0,classical,Standard
classical,0.31,1442.79,Standard,1567.0,classical,Standard
classical,0.32,1456.76,Standard,1572.0,classical,Standard
classical,0.33,1467.91,Standard,1577.0,classical,Standard
classical,0.34,1474.06,Standard,1582.0,classical,Standard
classical,0.35000000000000003,1482.0,Standard,1588.0,classical,Standard
classical,0.36000000000000004,1490.48,Standard,1593.0,classical,Standard
classical,0.37,1498.33,Standard,1599.0,classical,Standard
classical,0.38,1500.0,Standard,1604.0,classical,Standard
classical,0.39,1500.0,Standard,1610.0,classical,Standard
classical,0.4,1500.0,Standard,1616.0,classical,Standard
classical,0.41000000000000003,1500.0,Standard,1621.0,classical,Standard
classical,0.42000000000000004,1500.0,Standard,1627.0,classical,Standard
classical,0.43,1500.0,Standard,1633.0,classical,Standard
classical,0.44,1508.8799999999999,Standard,1639.0,classical,Standard
classical,0.45,1513.05,Standard,1644.0,classical,Standard
classical,0.46,1517.2800000000002,Standard,1650.0,classical,Standard
classical,0.47000000000000003,1526.23,Standard,1656.0,classical,Standard
classical,0.48000000000000004,1534.0,Standard,1662.0,classical,Standard
classical,0.49,1542.4099999999999,Standard,1667.0,classical,Standard
classical,0.5,1552.5,Standard,1673.0,classical,Standard
classical,0.51,1561.77,Standard,1680.0,classical,Standard
classical,0.52,1573.0,Standard,1686.0,classical,Standard
classical,0.53,1580.54,Standard,1692.0,classical,Standard
classical,0.54,1584.8600000000001,Standard,1699.0,classical,Standard
classical,0.55,1597.95,Standard,1705.0,classical,Standard
classical,0.56,1602.04,Standard,1712.0,classical,Standard
classical,0.5700000000000001,1611.0,Standard,1718.0,classical,Standard
classical,0.5800000000000001,1617.44,Standard,1725.0,classical,Standard
classical,0.59,1623.0,Standard,1732.0,classical,Standard
classical,0.6,1632.0,Standard,1738.0,classical,Standard
classical,0.61,1638.49,Standard,1744.0,classical,Standard
classical,0.62,1645.0,Standard,1752.0,classical,Standard
classical,0.63,1649.0,Standard,1759.0,classical,Standard
classical,0.64,1659.76,Standard,1765.0,classical,Standard
classical,0.65,1666.0,Standard,1773.0,classical,Standard
classical,0.66,1676.88,Standard,1780.0,classical,Standard
classical,0.67,1687.0,Standard,1786.0,classical,Standard
classical,0.68,1698.12,Standard,1794.0,classical,Standard
classical,0.6900000000000001,1713.21,Standard,1801.0,classical,Standard
classical,0.7000000000000001,1721.6,Standard,1809.0,classical,Standard
classical,0.7100000000000001,1727.7800000000004,Standard,1816.0,classical,Standard
classical,0.72,1734.48,Standard,1823.5999999999985,classical,Standard
classical,0.73,1742.57,Standard,1830.0,classical,Standard
classical,0.74,1747.32,Standard,1838.0,classical,Standard
classical,0.75,1756.75,Standard,1846.0,classical,Standard
classical,0.76,1767.8400000000001,Standard,1855.0,classical,Standard
classical,0.77,1778.93,Standard,1864.0,classical,Standard
classical,0.78,1787.0,Standard,1873.0,classical,Standard
classical,0.79,1796.0,Standard,1881.0,classical,Standard
classical,0.8,1801.2,Standard,1891.0,classical,Standard
classical,0.81,1808.29,Standard,1900.0,classical,Standard
classical,0.8200000000000001,1818.52,Standard,1909.0,classical,Standard
classical,0.8300000000000001,1831.4699999999998,Standard,1918.0,classical,Standard
classical,0.8400000000000001,1839.0,Standard,1929.0,classical,Standard
classical,0.85,1857.3,Standard,1940.0,classical,Standard
classical,0.86,1871.48,Standard,1951.0,classical,Standard
classical,0.87,1883.4900000000002,Standard,1963.0,classical,Standard
classical,0.88,1891.92,Standard,1974.0,classical,Standard
classical,0.89,1896.02,Standard,1987.0,classical,Standard
classical,0.9,1911.3000000000002,Standard,2003.0,classical,Standard
classical,0.91,1924.7600000000002,Standard,2021.0,classical,Standard
classical,0.92,1941.2800000000002,Standard,2044.0,classical,Standard
classical,0.93,1955.85,Standard,2067.0,classical,Standard
classical,0.9400000000000001,1968.8399999999997,Standard,2092.0,classical,Standard
classical,0.9500000000000001,1994.3999999999996,Standard,2121.0,classical,Standard
classical,0.9600000000000001,2024.6400000000003,Standard,2152.0,classical,Standard
classical,0.97,2062.46,Standard,2193.0,classical,Standard
classical,0.98,2164.9399999999987,Standard,2243.0,classical,Standard
classical,0.99,2241.91,Standard,2323.0,classical,Standard
classical,1.0,2825.0,Standard,2751.0,classical,Standard
"""
mapping_df = pd.read_csv(StringIO(csv_data))

# ===============================
# Streamlit: Time control selection
# ===============================
time_control_labels = ["bullet", "blitz", "rapid", "classical"]
selected_tc = st.selectbox("Select Time Control to Compare:", time_control_labels, index=1)

# ===============================
# Filter for selected time control
# ===============================
subset = mapping_df[mapping_df["lichess_tc"] == selected_tc]

if subset.empty:
    st.warning(f"No data available for {selected_tc}")
else:
    # Compute correlation & regression line
    corr = subset["rating_lichess"].corr(subset["rating_fide"])
    slope, intercept = np.polyfit(subset["rating_lichess"], subset["rating_fide"], 1)
    reg_line = slope * subset["rating_lichess"] + intercept

    # Plot percentiles scatter
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=subset["rating_lichess"],
        y=subset["rating_fide"],
        mode="markers",
        name="Percentiles",
        marker=dict(size=6, color=subset["percentile"], colorscale="Viridis", showscale=True)
    ))
    fig.add_trace(go.Scatter(
        x=subset["rating_lichess"],
        y=reg_line,
        mode="lines",
        name=f"Trendline (r={corr:.2f})",
        line=dict(color="red", width=2)
    ))
    fig.update_layout(
        title=f"Lichess {selected_tc.capitalize()} → FIDE {subset['fide_tc'].iloc[0]} Ratings by Percentile",
        xaxis_title="Lichess Rating",
        yaxis_title="FIDE Rating",
        template="plotly_dark",
        xaxis=dict(tick0=0, dtick=200),
        yaxis=dict(tick0=0, dtick=200),
        height=600
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(f"**Correlation (r):** {corr:.3f} | **Slope:** {slope:.3f} | **Intercept:** {intercept:.1f}")

# ===============================
# Compare all time controls side by side
# ===============================
with st.expander("Compare All Time Controls Side by Side"):
    for tc in time_control_labels:
        subset_tc = mapping_df[mapping_df["lichess_tc"] == tc]
        if subset_tc.empty:
            st.write(f"No data for {tc}")
            continue
        corr_tc = subset_tc["rating_lichess"].corr(subset_tc["rating_fide"])
        slope_tc, intercept_tc = np.polyfit(subset_tc["rating_lichess"], subset_tc["rating_fide"], 1)
        reg_line_tc = slope_tc * subset_tc["rating_lichess"] + intercept_tc

        fig_tc = go.Figure()
        fig_tc.add_trace(go.Scatter(
            x=subset_tc["rating_lichess"],
            y=subset_tc["rating_fide"],
            mode="markers",
            name="Percentiles",
            marker=dict(size=6, color=subset_tc["percentile"], colorscale="Viridis", showscale=True)
        ))
        fig_tc.add_trace(go.Scatter(
            x=subset_tc["rating_lichess"],
            y=reg_line_tc,
            mode="lines",
            name=f"Trendline (r={corr_tc:.2f})",
            line=dict(color="red", width=2)
        ))
        fig_tc.update_layout(
            title=f"{tc.capitalize()} → {subset_tc['fide_tc'].iloc[0]} Ratings",
            xaxis_title="Lichess Rating",
            yaxis_title="FIDE Rating",
            template="plotly_dark",
            xaxis=dict(tick0=0, dtick=200),
            yaxis=dict(tick0=0, dtick=200),
            height=500
        )
        st.plotly_chart(fig_tc, use_container_width=True)
        st.markdown(f"**{tc.capitalize()} correlation (r):** {corr_tc:.3f}")

# ===============================
# Combined plot of all time controls
# ===============================
with st.expander("Combined Plot for All Time Controls"):
    fig_combined = go.Figure()
    colors = {"bullet":"orange", "blitz":"blue", "rapid":"green", "classical":"purple"}

    for tc in time_control_labels:
        subset_tc = mapping_df[mapping_df["lichess_tc"] == tc]
        if subset_tc.empty:
            continue
        slope_tc, intercept_tc = np.polyfit(subset_tc["rating_lichess"], subset_tc["rating_fide"], 1)
        reg_line_tc = slope_tc * subset_tc["rating_lichess"] + intercept_tc

        fig_combined.add_trace(go.Scatter(
            x=subset_tc["rating_lichess"],
            y=subset_tc["rating_fide"],
            mode="markers",
            name=f"{tc.capitalize()} Percentiles",
            marker=dict(size=5, color=colors[tc])
        ))
        fig_combined.add_trace(go.Scatter(
            x=subset_tc["rating_lichess"],
            y=reg_line_tc,
            mode="lines",
            name=f"{tc.capitalize()} Trendline",
            line=dict(color=colors[tc], width=2)
        ))

    fig_combined.update_layout(
        title="Lichess → FIDE Ratings Across All Time Controls",
        xaxis_title="Lichess Rating",
        yaxis_title="FIDE Rating",
        template="plotly_dark",
        xaxis=dict(tick0=0, dtick=200),
        yaxis=dict(tick0=0, dtick=200),
        height=700
    )
    st.plotly_chart(fig_combined, use_container_width=True)


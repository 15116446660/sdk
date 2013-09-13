# Copyright (c) 2013, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

# This file contains all sources (vm and tests) for the dart virtual machine.
# Unit test files need to have a '_test' suffix appended to the name.
{
  'sources': [
    'allocation.cc',
    'allocation.h',
    'allocation_test.cc',
    'assembler.cc',
    'assembler.h',
    'assembler_arm.cc',
    'assembler_arm.h',
    'assembler_arm_test.cc',
    'assembler_ia32.cc',
    'assembler_ia32.h',
    'assembler_ia32_test.cc',
    'assembler_mips.cc',
    'assembler_mips.h',
    'assembler_mips_test.cc',
    'assembler_test.cc',
    'assembler_x64.cc',
    'assembler_x64.h',
    'assembler_x64_test.cc',
    'assert_test.cc',
    'ast.cc',
    'ast.h',
    'ast_printer.cc',
    'ast_printer.h',
    'ast_printer_test.cc',
    'ast_test.cc',
    'base_isolate.h',
    'benchmark_test.cc',
    'benchmark_test.h',
    'bigint_operations.cc',
    'bigint_operations.h',
    'bigint_operations_test.cc',
    'bit_vector.cc',
    'bit_vector.h',
    'bit_vector_test.cc',
    'bitfield.h',
    'bitfield_test.cc',
    'bitmap.cc',
    'bitmap.h',
    'bitmap_test.cc',
    'block_scheduler.cc',
    'block_scheduler.h',
    'boolfield.h',
    'boolfield_test.cc',
    'bootstrap.h',
    'bootstrap_natives.cc',
    'bootstrap_natives.h',
    'cha.cc',
    'cha.h',
    'cha_test.cc',
    'class_finalizer.cc',
    'class_finalizer.h',
    'class_finalizer_test.cc',
    'class_table.cc',
    'class_table.h',
    'code_descriptors.cc',
    'code_descriptors.h',
    'code_descriptors_test.cc',
    'code_generator.cc',
    'code_generator.h',
    'code_generator_test.cc',
    'code_observers.cc',
    'code_observers.h',
    'code_patcher.cc',
    'code_patcher.h',
    'code_patcher_arm.cc',
    'code_patcher_arm_test.cc',
    'code_patcher_ia32.cc',
    'code_patcher_ia32_test.cc',
    'code_patcher_mips.cc',
    'code_patcher_mips_test.cc',
    'code_patcher_x64.cc',
    'code_patcher_x64_test.cc',
    'compiler.cc',
    'compiler.h',
    'compiler_stats.cc',
    'compiler_stats.h',
    'compiler_test.cc',
    'constants_arm.h',
    'constants_ia32.h',
    'constants_mips.h',
    'constants_x64.h',
    'coverage.cc',
    'coverage.h',
    'cpu.h',
    'cpu_arm.cc',
    'cpu_ia32.cc',
    'cpu_mips.cc',
    'cpu_test.cc',
    'cpu_x64.cc',
    'custom_isolate_test.cc',
    'dart.cc',
    'dart.h',
    'dart_api_impl.h',
    'dart_api_impl_test.cc',
    'dart_api_message.cc',
    'dart_api_message.h',
    'dart_api_state.h',
    'dart_entry.cc',
    'dart_entry.h',
    'dart_entry_test.cc',
    'debugger.cc',
    'debugger.h',
    'debugger_api_impl_test.cc',
    'debugger_arm.cc',
    'debugger_ia32.cc',
    'debugger_mips.cc',
    'debugger_x64.cc',
    'debuginfo.h',
    'debuginfo_android.cc',
    'debuginfo_linux.cc',
    'deopt_instructions.cc',
    'deopt_instructions.h',
    'disassembler.cc',
    'disassembler.h',
    'disassembler_arm.cc',
    'disassembler_ia32.cc',
    'disassembler_mips.cc',
    'disassembler_test.cc',
    'disassembler_x64.cc',
    'double_conversion.cc',
    'double_conversion.h',
    'exceptions.cc',
    'exceptions.h',
    'exceptions_test.cc',
    'find_code_object_test.cc',
    'flags.cc',
    'flags.h',
    'flags_test.cc',
    'flow_graph.cc',
    'flow_graph.h',
    'flow_graph_allocator.cc',
    'flow_graph_allocator.h',
    'flow_graph_builder.cc',
    'flow_graph_builder.h',
    'flow_graph_compiler.cc',
    'flow_graph_compiler.h',
    'flow_graph_compiler_arm.cc',
    'flow_graph_compiler_ia32.cc',
    'flow_graph_compiler_mips.cc',
    'flow_graph_compiler_x64.cc',
    'flow_graph_inliner.cc',
    'flow_graph_inliner.h',
    'flow_graph_optimizer.cc',
    'flow_graph_optimizer.h',
    'flow_graph_type_propagator.cc',
    'flow_graph_type_propagator.h',
    'freelist.cc',
    'freelist.h',
    'freelist_test.cc',
    'gc_marker.cc',
    'gc_marker.h',
    'gc_sweeper.cc',
    'gc_sweeper.h',
    'gdbjit_android.cc',
    'gdbjit_android.h',
    'gdbjit_linux.cc',
    'gdbjit_linux.h',
    'globals.h',
    'growable_array.h',
    'growable_array_test.cc',
    'guard_field_test.cc',
    'handles.cc',
    'handles.h',
    'handles_impl.h',
    'handles_test.cc',
    'hash_map.h',
    'hash_map_test.cc',
    'heap.cc',
    'heap.h',
    'heap_histogram.cc',
    'heap_histogram.h',
    'heap_profiler.cc',
    'heap_profiler.h',
    'heap_profiler_test.cc',
    'heap_test.cc',
    'il_printer.cc',
    'il_printer.h',
    'instructions.h',
    'instructions_arm.cc',
    'instructions_arm.h',
    'instructions_arm_test.cc',
    'instructions_ia32.cc',
    'instructions_ia32.h',
    'instructions_ia32_test.cc',
    'instructions_mips.cc',
    'instructions_mips.h',
    'instructions_mips_test.cc',
    'instructions_x64.cc',
    'instructions_x64.h',
    'instructions_x64_test.cc',
    'intermediate_language.cc',
    'intermediate_language.h',
    'intermediate_language_arm.cc',
    'intermediate_language_ia32.cc',
    'intermediate_language_mips.cc',
    'intermediate_language_test.cc',
    'intermediate_language_x64.cc',
    'intrinsifier.cc',
    'intrinsifier.h',
    'intrinsifier_arm.cc',
    'intrinsifier_ia32.cc',
    'intrinsifier_mips.cc',
    'intrinsifier_x64.cc',
    'isolate.cc',
    'isolate.h',
    'isolate_test.cc',
    'json_stream.h',
    'json_stream.cc',
    'json_test.cc',
    'locations.cc',
    'locations.h',
    'longjump.cc',
    'longjump.h',
    'longjump_test.cc',
    'megamorphic_cache_table.cc',
    'megamorphic_cache_table.h',
    'memory_region.cc',
    'memory_region.h',
    'memory_region_test.cc',
    'message.cc',
    'message.h',
    'message_handler.cc',
    'message_handler.h',
    'message_handler_test.cc',
    'message_test.cc',
    'native_arguments.h',
    'native_entry.cc',
    'native_entry.h',
    'native_entry_test.cc',
    'native_entry_test.h',
    'native_message_handler.cc',
    'native_message_handler.h',
    'object.cc',
    'object.h',
    'object_arm_test.cc',
    'object_ia32_test.cc',
    'object_id_ring.cc',
    'object_id_ring.h',
    'object_id_ring_test.cc',
    'object_mips_test.cc',
    'object_store.cc',
    'object_store.h',
    'object_store_test.cc',
    'object_test.cc',
    'object_x64_test.cc',
    'os.h',
    'os_android.cc',
    'os_linux.cc',
    'os_macos.cc',
    'os_test.cc',
    'os_win.cc',
    'pages.cc',
    'pages.h',
    'pages_test.cc',
    'parser.cc',
    'parser.h',
    'parser_test.cc',
    'port.cc',
    'port.h',
    'port_test.cc',
    'raw_object.cc',
    'raw_object.h',
    'raw_object_snapshot.cc',
    'resolver.cc',
    'resolver.h',
    'resolver_test.cc',
    'reusable_handles.h',
    'runtime_entry.h',
    'runtime_entry_arm.cc',
    'runtime_entry_ia32.cc',
    'runtime_entry_mips.cc',
    'runtime_entry_test.cc',
    'runtime_entry_x64.cc',
    'scanner.cc',
    'scanner.h',
    'scanner_test.cc',
    'scavenger.cc',
    'scavenger.h',
    'scopes.cc',
    'scopes.h',
    'scopes_test.cc',
    'service.cc',
    'service.h',
    'simulator.h',
    'simulator_arm.cc',
    'simulator_arm.h',
    'simulator_mips.cc',
    'simulator_mips.h',
    'snapshot.cc',
    'snapshot.h',
    'snapshot_ids.h',
    'snapshot_test.cc',
    'stack_frame.cc',
    'stack_frame.h',
    'stack_frame_arm.h',
    'stack_frame_ia32.h',
    'stack_frame_mips.h',
    'stack_frame_test.cc',
    'stack_frame_x64.h',
    'store_buffer.cc',
    'store_buffer.h',
    'stub_code.cc',
    'stub_code.h',
    'stub_code_arm.cc',
    'stub_code_arm_test.cc',
    'stub_code_ia32.cc',
    'stub_code_ia32_test.cc',
    'stub_code_mips.cc',
    'stub_code_mips_test.cc',
    'stub_code_x64.cc',
    'stub_code_x64_test.cc',
    'symbols.cc',
    'symbols.h',
    'thread.h',
    'thread_pool.cc',
    'thread_pool.h',
    'thread_pool_test.cc',
    'thread_test.cc',
    'timer.cc',
    'timer.h',
    'token.cc',
    'token.h',
    'unicode.cc',
    'unicode.h',
    'unicode_data.cc',
    'unicode_test.cc',
    'unit_test.cc',
    'unit_test.h',
    'utils_test.cc',
    'verifier.cc',
    'verifier.h',
    'virtual_memory.cc',
    'virtual_memory.h',
    'virtual_memory_android.cc',
    'virtual_memory_linux.cc',
    'virtual_memory_macos.cc',
    'virtual_memory_test.cc',
    'virtual_memory_win.cc',
    'visitor.h',
    'vtune.cc',
    'vtune.h',
    'weak_table.cc',
    'weak_table.h',
    'zone.cc',
    'zone.h',
    'zone_test.cc',
  ],
}
